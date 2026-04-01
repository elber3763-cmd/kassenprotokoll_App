@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Kassenprotokoll - EXE Build
echo ===================================================
echo   Kassenprotokoll App - EXE aktualisieren
echo ===================================================
echo.

echo [1/3] Beende laufende Instanz...
taskkill /f /im kassenprotokoll.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/3] Bereinige alte Dateien...
if exist "build" rmdir /s /q "build"
if exist "dist\kassenprotokoll.exe" del /f /q "dist\kassenprotokoll.exe"

echo [3/3] Starte PyInstaller...
echo        (Das kann 1-2 Minuten dauern)
echo.
.venv\Scripts\python.exe -m PyInstaller kassenprotokoll.spec -y --distpath "dist" --clean
if errorlevel 1 (
    echo.
    echo ===================================================
    echo   FEHLER: Build fehlgeschlagen!
    echo ===================================================
    pause
    exit /b 1
)

if exist "build" rmdir /s /q "build"

echo.
echo ===================================================
echo   BUILD ERFOLGREICH!
echo   EXE: %CD%\dist\kassenprotokoll.exe
echo ===================================================
echo.
pause
