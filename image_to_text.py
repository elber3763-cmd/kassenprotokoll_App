from PIL import Image
import pytesseract
import os

# --- Tesseract OCR Konfiguration ---
# Der korrekte Pfad zu Ihrer Tesseract-Installation Version 5.5.0:
pytesseract.pytesseract.tesseract_cmd = r'C:\OCR\tesseract.exe' # <--- PFAD WURDE AKTUALISIERT!

def image_to_text(image_path, lang='deu'):
    """
    Konvertiert ein Bild in Text mithilfe von Tesseract OCR.

    Args:
        image_path (str): Der Pfad zum Eingabebild.
        lang (str): Die Sprache des Textes im Bild (z.B. 'deu' für Deutsch, 'eng' für Englisch).

    Returns:
        str: Der extrahierte Text aus dem Bild.
    """
    if not os.path.exists(image_path):
        return f"FEHLER: Bilddatei nicht gefunden unter {image_path}"

    try:
        img = Image.open(image_path)
        # 'deu' für deutsche Sprache. Stellen Sie sicher, dass das deutsche Sprachpaket mit Tesseract installiert ist.
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except pytesseract.TesseractNotFoundError:
        return "FEHLER: Tesseract OCR Engine wurde nicht gefunden. Bitte stellen Sie sicher, dass Tesseract installiert und im PATH ist oder der Pfad in pytesseract.pytesseract.tesseract_cmd korrekt gesetzt ist."
    except Exception as e:
        return f"FEHLER: Ein unerwarteter Fehler ist aufgetreten: {e}. Überprüfen Sie Tesseract-Pfad und Bildformat."

if __name__ == "__main__":
    # --- Beispiel-Nutzung (Dieser Teil wird nur ausgeführt, wenn Sie diese Datei direkt starten) ---
    my_image_path = "beispielbild_mit_text.png" # <--- HIER DEN PFAD ANPASSEN, wenn Sie dies direkt testen!

    print(f"Bitte passen Sie 'my_image_path' in '{__file__}' an, um eine Bilddatei zu testen.")