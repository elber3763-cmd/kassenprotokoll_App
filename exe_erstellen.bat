@echo off
setlocal
title Kassenprotokoll EXE-Builder
color 0A

:: --- KONFIGURATION ---
set "PROJEKT_PFAD=O:\kassenprotokoll_App"

:: Zum Projektpfad wechseln
cd /d "%PROJEKT_PFAD%"

echo.
echo ========================================================
echo   SCHRITT 1: BEREINIGUNG
echo ========================================================
echo Loesche alte Ordner (venv, build, dist) und Spec-Dateien...

if exist "venv" (
    echo - Entferne venv...
    rmdir /s /q "venv"
)
if exist "build" (
    echo - Entferne build...
    rmdir /s /q "build"
)
if exist "dist" (
    echo - Entferne dist...
    rmdir /s /q "dist"
)
if exist "kassenprotokoll.spec" (
    echo - Entferne kassenprotokoll.spec...
    del /f /q "kassenprotokoll.spec"
)

echo.
echo ========================================================
echo   SCHRITT 2: VENV ERSTELLEN
echo ========================================================
echo Erstelle neue virtuelle Umgebung...
python -m venv venv

if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo.
    echo [FEHLER] Python konnte nicht gefunden werden.
    echo Stellen Sie sicher, dass Python installiert und im PATH ist.
    pause
    exit /b
)

echo.
echo ========================================================
echo   SCHRITT 3: PAKETE INSTALLIEREN
echo ========================================================
echo Upgrade PIP...
".\venv\Scripts\python.exe" -m pip install --no-cache-dir --upgrade pip

echo Installiere Abhaengigkeiten...
".\venv\Scripts\pip.exe" install --no-cache-dir PyInstaller fpdf2 python-docx openpyxl pygame pywin32 asteval Pillow PyMuPDF ttkthemes pillow-avif-plugin

if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo.
    echo [FEHLER] Bei der Installation der Pakete ist ein Fehler aufgetreten.
    pause
    exit /b
)

echo.
echo ========================================================
echo   SCHRITT 4: EXE ERSTELLEN (PyInstaller)
echo ========================================================
echo Starte Build-Prozess...

".\venv\Scripts\python.exe" -m PyInstaller --noconfirm --windowed --clean ^
 --additional-hooks-dir hooks ^
 --hidden-import PIL._tkinter_finder ^
 --hidden-import fpdf ^
 --hidden-import fpdf.enums ^
 --hidden-import asteval ^
 --hidden-import fitz ^
 --hidden-import pillow_avif ^
 --add-data "fonts;fonts" ^
 --add-data "icons;icons" ^
 --add-data "images/slideshow;images/slideshow" ^
 kassenprotokoll.py

if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo.
    echo [FEHLER] PyInstaller wurde mit Fehlern beendet.
    pause
    exit /b
)

echo.
echo ========================================================
echo   FERTIG!
echo ========================================================
echo Die neue EXE-Datei befindet sich im Ordner:
echo %PROJEKT_PFAD%\dist\kassenprotokoll
echo.
pause