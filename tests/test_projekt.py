"""Eigene synthetische Regressionstests ohne Schul- oder Personendaten."""
from __future__ import annotations
import importlib.util
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
logic=load('worksheet_logic',ROOT/'arbeitsblatt-generator/scripts/worksheet_logic.py')
build=load('paket_bauen',ROOT/'tools/paket_bauen.py')

def task(ident,topic='addieren',deps=None):
    return {'id':ident,'topic':topic,'stage':0,'family':'zeile',
            'difficulty':[1,1],'minutes':2,'depends_on':deps or []}

def plan(tasks,topics=None):
    return {'school':'VS','class':3,'topic_order':topics or ['addieren'],'tasks':tasks}

def block(ident,y=20):
    return {'id':ident,'page':1,'bbox_mm':[15,y,180,25]}

class PlanungUndLayout(unittest.TestCase):
    def test_schulprofil(self):
        self.assertEqual(logic.school_profile('VS',3)['grade'],3)
        self.assertEqual(logic.school_profile('MS',2)['grade'],6)
    def test_unzulaessige_klasse(self):
        with self.assertRaises(ValueError): logic.school_profile('VS',True)
        with self.assertRaises(ValueError): logic.school_profile('VS',5)
    def test_abhaengigkeit(self):
        out=logic.sort_tasks(plan([task('b',deps=['a']),task('a')]))
        self.assertEqual(out['ordered_ids'],['a','b'])
    def test_zyklus_abweisen(self):
        with self.assertRaises(ValueError):
            logic.sort_tasks(plan([task('a',deps=['b']),task('b',deps=['a'])]))
    def test_doppelte_id_abweisen(self):
        with self.assertRaises(ValueError): logic.sort_tasks(plan([task('a'),task('a')]))
    def test_themenkonflikt_abweisen(self):
        with self.assertRaises(ValueError):
            logic.sort_tasks(plan([task('a',deps=['b']),task('b','multiplizieren')],
                                  ['addieren','multiplizieren']))
    def test_layout_ok(self):
        out=logic.check_layout({'blocks':[block('a'),block('b',55)]})
        self.assertTrue(out['ok'])
    def test_layout_ueberlappung(self):
        out=logic.check_layout({'blocks':[block('a'),block('b',30)]})
        self.assertFalse(out['ok'])
    def test_layout_schreibraum(self):
        a=block('a');a.update(flow_mm=[5,10],writing=[{
            'required_width_mm':100,'available_width_mm':30,
            'required_lines':2,'available_lines':1}])
        self.assertFalse(logic.check_layout({'blocks':[a]})['ok'])
    def test_layout_innenhoehe(self):
        a=block('a');a['flow_mm']=[10,[15,20],5]
        self.assertFalse(logic.check_layout({'blocks':[a]})['ok'])
    def test_layout_rand(self):
        a=block('a');a['bbox_mm']=[2,20,180,25]
        self.assertFalse(logic.check_layout({'blocks':[a]})['ok'])

class Paketbau(unittest.TestCase):
    def test_zip_wiederholbar(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d)/'arbeitsblatt-generator';folder.mkdir()
            (folder/'SKILL.md').write_text('Beispiel',encoding='utf-8')
            first=build.zip_bytes(folder)
            self.assertEqual(first,build.zip_bytes(folder))
            with zipfile.ZipFile(io.BytesIO(first)) as z:
                self.assertEqual(z.namelist(),['arbeitsblatt-generator/SKILL.md'])
    def test_gleiche_datei_erlauben(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'skill.zip';build.write_once(p,b'a');build.write_once(p,b'a')
            self.assertEqual(p.read_bytes(),b'a')
    def test_ueberschreiben_verhindern(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'skill.zip';build.write_once(p,b'a')
            with self.assertRaises(ValueError): build.write_once(p,b'b')
            self.assertEqual(p.read_bytes(),b'a')
    def test_symlink_abweisen(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d)/'arbeitsblatt-generator';folder.mkdir()
            (folder/'link').symlink_to('nicht_vorhanden')
            with self.assertRaises(ValueError): build.zip_bytes(folder)

if __name__=='__main__': unittest.main()
