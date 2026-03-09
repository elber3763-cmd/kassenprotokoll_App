# Custom override: suppress the broken hook-cryptography.py from pyinstaller-hooks-contrib
# which crashes on Python 3.13 free-threaded builds due to an OpenSSL/isolated-subprocess issue.
# cryptography is only a transitive dependency and doesn't need special collection.
hiddenimports = []
datas = []
binaries = []
