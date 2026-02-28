# hook-pywin32.py
from PyInstaller.utils.hooks import collect_dynamic_libs

# This hook tells PyInstaller to find and bundle the essential DLLs
# that pywin32 often places in non-standard locations.
binaries = collect_dynamic_libs('pywintypes') + collect_dynamic_libs('pythoncom')