import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import pytesseract
import os

# --- Tesseract OCR Konfiguration ---
# Der korrekte Pfad zu Ihrer Tesseract-Installation Version 5.5.0:
pytesseract.pytesseract.tesseract_cmd = r'C:\OCR\tesseract.exe' # <--- PFAD WURDE AKTUALISIERT!
#
# Stellen Sie auch sicher, dass die benötigten Sprachpakete (z.B. 'deu.traineddata')
# in Ihrer Tesseract-Installation vorhanden sind.

# --- OCR-Funktion (wie zuvor, leicht angepasst) ---
def extract_text_from_image(image_path, lang='deu'):
    """
    Konvertiert ein Bild in Text mithilfe von Tesseract OCR.
    """
    if not os.path.exists(image_path):
        return f"FEHLER: Bilddatei nicht gefunden unter {image_path}"

    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except pytesseract.TesseractNotFoundError:
        return "FEHLER: Tesseract OCR Engine nicht gefunden. Bitte prüfen Sie die Installation, den PATH oder ob der Pfad in pytesseract.pytesseract.tesseract_cmd korrekt gesetzt ist."
    except Exception as e:
        # Fügen Sie hier zusätzliche Informationen hinzu, um den genauen Fehler von Tesseract zu sehen
        return f"FEHLER: Ein unerwarteter Fehler ist aufgetreten: {e}. Überprüfen Sie Tesseract-Pfad und Bildformat."

# --- GUI-Anwendung ---
class OCRApp:
    def __init__(self, master):
        self.master = master
        master.title("Bild-zu-Text (OCR) App")
        master.geometry("800x600")

        # --- DIAGNOSE-INFORMATIONEN ZUM START (jetzt sollten sie die korrekte Version zeigen) ---
        print(f"DEBUG: Tesseract CMD Pfad im Code: {pytesseract.pytesseract.tesseract_cmd}")
        try:
            tesseract_version = pytesseract.get_tesseract_version()
            print(f"DEBUG: Von pytesseract erkannte Tesseract Version: {tesseract_version}")
        except pytesseract.TesseractNotFoundError:
            print("DEBUG: Tesseract nicht über pytesseract.get_tesseract_version() gefunden.")
        except Exception as e:
            print(f"DEBUG: Fehler beim Abrufen der Tesseract-Version: {e}")
        # --- ENDE DIAGNOSE-INFORMATIONEN ---

        master.columnconfigure(0, weight=1)
        master.rowconfigure(2, weight=1)

        self.selection_frame = ttk.LabelFrame(master, text="Bild auswählen", padding="10")
        self.selection_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.selection_frame.columnconfigure(0, weight=1)

        self.file_path_label = ttk.Label(self.selection_frame, text="Keine Datei ausgewählt.")
        self.file_path_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.browse_button = ttk.Button(self.selection_frame, text="Bild auswählen", command=self.browse_image)
        self.browse_button.grid(row=0, column=1, padx=5, pady=5)

        self.language_frame = ttk.LabelFrame(master, text="Sprache für OCR", padding="10")
        self.language_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.language_frame.columnconfigure(1, weight=1)

        ttk.Label(self.language_frame, text="Sprache:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.lang_var = tk.StringVar(value='deu')
        self.lang_combobox = ttk.Combobox(self.language_frame, textvariable=self.lang_var,
                                          values=['deu', 'eng', 'fra', 'spa', 'ita'],
                                          state="readonly")
        self.lang_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.lang_combobox.set('deu')

        self.text_output_frame = ttk.LabelFrame(master, text="Extrahierter Text", padding="10")
        self.text_output_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        self.text_output_frame.columnconfigure(0, weight=1)
        self.text_output_frame.rowconfigure(0, weight=1)

        self.text_output = tk.Text(self.text_output_frame, wrap="word", height=15)
        self.text_output.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.text_output_frame, command=self.text_output.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_output.config(yscrollcommand=self.scrollbar.set)

        self.status_label = ttk.Label(master, text="Bereit.", relief=tk.SUNKEN, anchor="w")
        self.status_label.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            title="Bild zum Extrahieren auswählen",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff"), ("All Files", "*.*")]
        )
        if file_path:
            self.file_path_label.config(text=file_path)
            self.status_label.config(text="Bild wird verarbeitet...", foreground="blue")
            self.master.update_idletasks()

            self.perform_ocr(file_path)

    def perform_ocr(self, image_path):
        lang = self.lang_var.get()
        extracted_text = extract_text_from_image(image_path, lang=lang)

        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, extracted_text)

        if extracted_text.startswith("FEHLER"):
            self.status_label.config(text=f"OCR Fehler!", foreground="red")
            messagebox.showerror("OCR Fehler", extracted_text)
        else:
            self.status_label.config(text="OCR abgeschlossen.", foreground="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()