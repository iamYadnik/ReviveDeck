# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['revivedeck.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui/*', 'ui'),
        ('config/*', 'config'),
        ('scripts/*', 'scripts'),
        ('plugins/*', 'plugins'),
        ('assets/*', 'assets')
    ],
    hiddenimports=collect_submodules('PyQt5'),
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=False,
    name='revivedeck',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='assets/revivedeck_icon.png' if sys.platform.startswith('win') else None
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='revivedeck'
)