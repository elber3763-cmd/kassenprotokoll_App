# hook-pywin32.py
# Includes pywin32 DLLs (pythoncom313.dll, pywintypes313.dll) so that
# win32com Outlook automation works in the bundled EXE.
import os, glob

_lib = os.path.dirname(os.__file__)
_sys32 = os.path.join(_lib, 'site-packages', 'pywin32_system32')

# Include DLLs as binaries so they land next to the EXE
binaries = [(dll, '.') for dll in glob.glob(os.path.join(_sys32, '*.dll'))]
datas = []
hiddenimports = []
