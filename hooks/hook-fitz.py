# Custom hook for fitz/pymupdf — avoids isolated subprocess crash on Python 3.13t.
import os, glob
import importlib.util

hiddenimports = ['pymupdf', 'pymupdf.mupdf', 'fitz.utils', 'fitz.table']
datas = []

# Collect pymupdf binaries directly without triggering isolated subprocess
_spec = importlib.util.find_spec('pymupdf')
if _spec and _spec.submodule_search_locations:
    _dir = list(_spec.submodule_search_locations)[0]
    binaries = (
        [(f, 'pymupdf') for f in glob.glob(os.path.join(_dir, '*.pyd'))]
        + [(f, 'pymupdf') for f in glob.glob(os.path.join(_dir, '*.dll'))]
    )
else:
    binaries = []
