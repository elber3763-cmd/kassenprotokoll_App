# hook-pywin32.py
# Includes pywin32 DLLs (pythoncom313.dll, pywintypes313.dll) so that
# win32com Outlook automation works in the bundled EXE.
import os, glob, sys

# Find pywin32_system32 in the actual environment (venv or system)
_sys32 = ''
for path in sys.path:
    candidate = os.path.join(path, 'pywin32_system32')
    if os.path.isdir(candidate):
        _sys32 = candidate
        break

binaries = []
datas = []
hiddenimports = ['win32com', 'win32com.client', 'win32timezone', 'pythoncom', 'pywintypes']

if _sys32:
    # Place DLLs in pywin32_system32/ subdirectory (matches runtime hooks expectation)
    datas = [(dll, 'pywin32_system32') for dll in glob.glob(os.path.join(_sys32, '*.dll'))]
    # Also place in root for direct access
    datas += [(dll, '.') for dll in glob.glob(os.path.join(_sys32, '*.dll'))]
