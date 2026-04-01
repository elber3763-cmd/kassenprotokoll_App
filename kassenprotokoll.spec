# -*- mode: python ; coding: utf-8 -*-


import os, glob
_venv_sp = os.path.join('O:\\\\kassenprotokoll_App', '.venv', 'Lib', 'site-packages')
_pywin32_dlls = glob.glob(os.path.join(_venv_sp, 'pywin32_system32', '*.dll'))

a = Analysis(
    ['kassenprotokoll.py'],
    pathex=[],
    binaries=[(dll, '.') for dll in _pywin32_dlls],
    datas=[
        ('fonts', 'fonts'),
        ('icons', 'icons'),
        ('images', 'images'),
        ('sounds', 'sounds'),
    ],
    hiddenimports=['win32com', 'win32com.client', 'win32timezone', 'pythoncom', 'pywintypes', 'asteval'],
    hookspath=['hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='kassenprotokoll',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
