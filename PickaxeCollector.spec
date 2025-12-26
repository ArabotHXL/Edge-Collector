# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.building.datastruct import Tree

block_cipher = None

REPO_ROOT = Path.cwd()
ENTRY = str(REPO_ROOT / "pickaxe_app" / "__main__.py")

datas = [
    (str(REPO_ROOT / "pickaxe_app" / "web"), "pickaxe_app/web"),
]

hiddenimports = []
hiddenimports += collect_submodules("fastapi")
hiddenimports += collect_submodules("starlette")
hiddenimports += collect_submodules("uvicorn")
hiddenimports += collect_submodules("pydantic")

a = Analysis(
    [ENTRY],
    pathex=[str(REPO_ROOT)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
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
    strip=False,
    upx=True,
    console=True,
)
