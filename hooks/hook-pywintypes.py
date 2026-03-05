# Custom override: suppress the broken pyinstaller-hooks-contrib hook-pywintypes.py
# which crashes on Python 3.13 free-threaded builds.
# pywintypes is bundled via hook-pywin32.py via collect_dynamic_libs.
binaries = []
datas = []
hiddenimports = []
