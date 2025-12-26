# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.building.datastruct import Tree

block_cipher = None

# Robust repo root detection for GitHub Actions & local runs
REPO_ROOT = Path.cwd()
try:
    if "__file__" in globals():
        REPO_ROOT = Path(__file__).resolve().parent
except Exception:
    REPO_ROOT = Path.cwd()

ENTRY = str(REPO_ROOT / "pickaxe_app" / "__main__.py")

# Bundle UI assets (FastAPI mounts StaticFiles from pickaxe_app/web/static)
datas = [
    Tree(str(REPO_ROOT / "pickaxe_app" / "web"), prefix="pickaxe_app/web"),
]

hiddenimports = []
hiddenimports += collect_submodules("fastapi")
hiddenimports += collect_submodules("starlette")
hiddenimports += collect_submodules("pydantic")
hiddenimports += collect_submodules("uvicorn")

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
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
