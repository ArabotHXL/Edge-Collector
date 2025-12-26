# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

block_cipher = None

REPO_ROOT = Path(__file__).resolve().parent

# IMPORTANT:
# If your entry is different, change this line.
ENTRY = str(REPO_ROOT / "pickaxe_app" / "__main__.py")

if not Path(ENTRY).exists():
    raise SystemExit(
        f"[PickaxeCollector.spec] ENTRY not found: {ENTRY}\n"
        "Fix: update ENTRY to your real server entry (e.g. pickaxe_app/main.py or server.py)."
    )

# Include static assets if present
datas = []
for rel in [
    ("pickaxe_app/web", "pickaxe_app/web"),
    ("pickaxe_app/templates", "pickaxe_app/templates"),
    ("pickaxe_app/static", "pickaxe_app/static"),
]:
    src = REPO_ROOT / rel[0]
    if src.exists():
        datas.append((str(src), rel[1]))

# Hidden imports for FastAPI/Uvicorn
hiddenimports = [
    "fastapi",
    "uvicorn",
    "uvicorn.logging",
    "uvicorn.protocols.http.h11_impl",
    "uvicorn.protocols.websockets.websockets_impl",
]

from PyInstaller.utils.hooks import collect_submodules
hiddenimports += collect_submodules("fastapi")
hiddenimports += collect_submodules("uvicorn")

a = Analysis(
    [ENTRY],
    pathex=[str(REPO_ROOT)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="PickaxeCollector",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="PickaxeCollector",
)
