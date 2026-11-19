#!/usr/bin/env python3
"""Ein reproduzierbares Skill-ZIP mit Pruefsumme bauen; nichts hochladen."""
from __future__ import annotations
import hashlib
import io
import os
import subprocess
import sys
import zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'arbeitsblatt-generator'

def zip_bytes(folder: Path) -> bytes:
    buffer=io.BytesIO()
    with zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in sorted(folder.rglob('*')):
            if path.is_symlink():
                raise ValueError('Symbolischer Link im Paket nicht erlaubt.')
            if not path.is_file():
                continue
            if '__pycache__' in path.parts or path.suffix=='.pyc':
                raise ValueError('Python-Cache vor dem Paketbau entfernen.')
            name=(Path(folder.name)/path.relative_to(folder)).as_posix()
            info=zipfile.ZipInfo(name,date_time=(2020,1,1,0,0,0))
            info.create_system=3
            info.external_attr=0o100644 << 16
            info.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(info,path.read_bytes(),compresslevel=9)
    return buffer.getvalue()

def write_once(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    try:
        with path.open('xb') as output:
            output.write(data)
    except FileExistsError:
        if path.read_bytes()!=data:
            raise ValueError('Bestehende Version nicht ueberschreiben; neue Version erforderlich: '+str(path))

def main() -> int:
    try:
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        subprocess.run([sys.executable,str(ROOT/'tools/pruefen.py')],check=True,env=env,timeout=120)
        version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
        payload=zip_bytes(SKILL)
        digest=hashlib.sha256(payload).hexdigest()
        dest=ROOT/'dist'/('v'+version)
        write_once(dest/'skill.zip',payload)
        write_once(dest/'SHA256SUMS',(digest+'  skill.zip\n').encode('ascii'))
        print('Paket erstellt oder bytegleich vorhanden: '+str(dest/'skill.zip'))
        print('SHA-256: '+digest)
        print('Nicht auf GitHub veroeffentlicht und nicht in einer KI-Plattform installiert.')
        return 0
    except (ValueError,OSError,subprocess.SubprocessError) as exc:
        print('PAKETBAU FEHLGESCHLAGEN: '+str(exc),file=sys.stderr)
        return 1
if __name__=='__main__':
    raise SystemExit(main())
