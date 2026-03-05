# Custom override: suppress the broken pyinstaller-hooks-contrib hook-pythoncom.py
# which crashes on Python 3.13 free-threaded builds.
# pythoncom is bundled via hook-pywin32.py via collect_dynamic_libs.
binaries = []
datas = []
hiddenimports = []
