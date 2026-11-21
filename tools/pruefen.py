#!/usr/bin/env python3
"""Lokale Struktur-, Versions-, Syntax- und Regressionstests. Kein Upload."""
from __future__ import annotations
import ast
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'arbeitsblatt-generator'
REQUIRED = ('SKILL.md', 'agents/openai.yaml', 'assets/icon.svg', 'VERSION',
            'LICENSE', 'LIZENZ.md', 'RECHTLICHES.md',
            'scripts/math_quality_gate.py', 'scripts/test_math_quality_gate.py',
            'scripts/worksheet_logic.py', 'references/mathematik.md',
            'references/deutsch.md', 'references/englisch.md',
            'references/rechte-datenschutz-plattformen.md')

def validate_structure() -> str:
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', version):
        raise ValueError('VERSION muss eine einfache Versionsnummer X.Y.Z enthalten.')
    for relative in REQUIRED:
        if not (SKILL / relative).is_file():
            raise ValueError('Pflichtdatei fehlt: '+relative)
    if (SKILL / 'VERSION').read_text(encoding='utf-8').strip() != version:
        raise ValueError('Versionsdateien stimmen nicht ueberein.')
    entry = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    header = re.match(r'^---\n(.*?)\n---\n',entry,re.S)
    if not header or not re.search(r'^name: arbeitsblatt-generator$',header[1],re.M):
        raise ValueError('SKILL.md: Kopf oder Skill-Name ungueltig.')
    if not re.search(r'^description: .+', header[1], re.M):
        raise ValueError('SKILL.md: Beschreibung fehlt.')
    if '**Paketversion: '+version+'**' not in entry:
        raise ValueError('Versionszeile in SKILL.md stimmt nicht.')
    if (ROOT/'LICENSE').read_bytes() != (SKILL/'LICENSE').read_bytes():
        raise ValueError('Lizenztexte stimmen nicht ueberein.')
    for p in SKILL.rglob('*'):
        if p.is_symlink():
            raise ValueError('Keine symbolischen Links im Skill: '+p.name)
        if p.is_file() and (p.suffix.lower() in ('.ttf','.otf','.woff','.woff2','.pyc')
                            or p.name.startswith('.env')):
            raise ValueError('Nicht zugelassene Paketdatei: '+p.name)
    for p in ROOT.rglob('*.py'):
        if 'dist' not in p.parts:
            ast.parse(p.read_text(encoding='utf-8'), filename=str(p.relative_to(ROOT)))
    for p in ROOT.rglob('*.md'):
        if 'dist' in p.parts:
            continue
        text=p.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
            if '://' in target or target.startswith(('#','mailto:')):
                continue
            rel=unquote(target.split('#',1)[0])
            if rel and not (p.parent/rel).exists():
                raise ValueError(f'Fehlender lokaler Verweis in {p.name}: {rel}')
    return version

def main() -> int:
    try:
        version=validate_structure()
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        commands = [
            [sys.executable, str(SKILL/'scripts/test_math_quality_gate.py')],
            [sys.executable, str(SKILL/'scripts/test_schriftliche_division.py')],
            [sys.executable, '-m', 'unittest', 'discover', '-s', str(ROOT/'tests'), '-v'],
        ]
        for command in commands:
            subprocess.run(command,cwd=ROOT,env=env,check=True,timeout=60)
        print('Struktur, Version, Python-Syntax, lokale Verweise und Regressionstests bestanden: '+version)
        print('Keine Aussage ueber PDF-Sichtpruefung, Bildbereinigung oder Zielinstallation.')
        return 0
    except (ValueError,OSError,SyntaxError,subprocess.SubprocessError) as exc:
        print('PRUEFUNG FEHLGESCHLAGEN: '+str(exc),file=sys.stderr)
        return 1
if __name__ == '__main__':
    raise SystemExit(main())
