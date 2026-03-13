@echo off
title Kassenprotokoll - Build
echo ===================================================
echo   Kassenprotokoll App - Build
echo ===================================================
echo.

echo [1/4] Beende laufende Instanz...
taskkill /f /im kassenprotokoll.exe 2>nul

echo [2/4] Bereinige Build-Ordner...
if exist "build" rmdir /s /q "build"
if exist "dist\kassenprotokoll.exe" del /f /q "dist\kassenprotokoll.exe"

echo [3/4] Starte PyInstaller...
venv\Scripts\pyinstaller.exe --clean --noconfirm ^
    --distpath "dist" ^
    kassenprotokoll.spec

echo [4/4] Fertig.
pause
