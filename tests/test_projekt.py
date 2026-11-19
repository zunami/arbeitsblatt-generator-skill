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

class VersionsUndFreigabe(unittest.TestCase):
    def test_lesbarer_release_titel_und_manueler_trigger(self):
        wf=(ROOT/'.github/workflows/release.yml').read_text(encoding='utf-8')
        self.assertIn('workflow_dispatch:',wf)
        self.assertIn('--title "Version ${RELEASE_VERSION}"',wf)
        self.assertIn('default: false',wf)
        self.assertIn('args+=(--prerelease)',wf)
        self.assertIn('args+=(--latest)',wf)
        self.assertIn('--notes-file "RELEASE_NOTES_v${RELEASE_VERSION}.md"',wf)
        self.assertNotIn('\n  push:',wf)
    def test_unveraenderlichkeit_und_pruefsumme(self):
        wf=(ROOT/'.github/workflows/release.yml').read_text(encoding='utf-8')
        self.assertIn('gh release view "$tag"',wf)
        self.assertIn('Tag existiert bereits',wf)
        self.assertIn('sha256sum --check SHA256SUMS',wf)
        self.assertIn('cmp --quiet',wf)
        self.assertIn('persist-credentials: false',wf)
    def test_version_ueberall_eindeutig(self):
        version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
        self.assertEqual(version,'0.1.2')
        self.assertIn('Version **'+version+'**', (ROOT/'README.md').read_text(encoding='utf-8'))
        self.assertIn('**Paketversion: '+version+'**',(ROOT/'arbeitsblatt-generator/SKILL.md').read_text(encoding='utf-8'))
        self.assertTrue((ROOT/('RELEASE_NOTES_v'+version+'.md')).exists())
    def test_fragen_nicht_routinemaessig(self):
        entry=(ROOT/'arbeitsblatt-generator/SKILL.md').read_text(encoding='utf-8')
        self.assertEqual(entry.count('## Grundsätze'),1)
        self.assertIn('Höchstens drei gebündelte',entry)
        self.assertIn('kein verpflichtender Sechs-Fragen-Dialog',entry)

if __name__=='__main__': unittest.main()
