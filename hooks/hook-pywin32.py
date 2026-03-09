# hook-pywin32.py
# Use 'datas' instead of 'binaries' for pywin32 DLLs to avoid isolated subprocess crash
# on Python 3.13t (free-threaded). The DLLs (pythoncom313.dll, pywintypes313.dll) are
# compiled against regular Python 3.13 (non-t), which causes an ABI crash when
# PyInstaller's isolated subprocess (running 3.13t) tries to import them for analysis.
import os, glob

_lib = os.path.dirname(os.__file__)
_sys32 = os.path.join(_lib, 'site-packages', 'pywin32_system32')

# Copy DLLs as data files (not binaries) to skip binary dependency analysis
datas = [(dll, '.') for dll in glob.glob(os.path.join(_sys32, '*.dll'))]
binaries = []
hiddenimports = []
