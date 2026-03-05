# Custom hook for psutil — avoids isolated subprocess crash on Python 3.13t.
import os, glob
import importlib.util

# Hardcode known submodules to avoid isolated subprocess
hiddenimports = [
    'psutil._pswindows',
    'psutil._psutil_windows',
    'psutil._common',
    'psutil._compat',
]
datas = []

# Collect .pyd binaries directly (no subprocess)
_spec = importlib.util.find_spec('psutil')
if _spec and _spec.submodule_search_locations:
    _psutil_dir = list(_spec.submodule_search_locations)[0]
    binaries = [(pyd, 'psutil') for pyd in glob.glob(os.path.join(_psutil_dir, '*.pyd'))]
else:
    binaries = []
