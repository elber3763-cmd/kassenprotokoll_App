# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['kassenprotokoll.py'],
    pathex=[],
    binaries=[],
    datas=[('fonts', 'fonts'), ('icons', 'icons'), ('images/slideshow', 'images/slideshow')],
    hiddenimports=[
        'PIL._tkinter_finder', 'fpdf', 'fpdf.enums', 'asteval', 'fitz', 'pillow_avif',
        'win32com', 'win32com.client', 'win32com.client.dynamic', 'win32com.client.gencache',
        'win32com.shell', 'win32com.shell.shell',
        'pywintypes', 'pythoncom', 'win32api', 'win32con',
    ],
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
    [],
    exclude_binaries=True,
    name='kassenprotokoll',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='kassenprotokoll',
)
