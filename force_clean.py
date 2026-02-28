import os
import shutil

# Wir starten die Suche eine Ebene höher, im "images"-Ordner
TARGET_ROOT = r"O:\kassenprotokoll_App\images"

def force_clean():
    print(f"!!! STARTE TIEFENREINIGUNG IN: {TARGET_ROOT} !!!")
    print("-" * 50)

    if not os.path.exists(TARGET_ROOT):
        print(f"FEHLER: Der Ordner {TARGET_ROOT} existiert nicht!")
        input("Enter...")
        return

    deleted_count = 0

    # os.walk geht rekursiv durch JEDEN Unterordner
    for current_folder, subfolders, filenames in os.walk(TARGET_ROOT, topdown=False):
        
        # Wir suchen in den Ordner-Namen
        for folder_name in subfolders:
            # Prüfen ob 'pycache' im Namen steckt (egal ob groß/klein)
            if "pycache" in folder_name.lower():
                full_path = os.path.join(current_folder, folder_name)
                print(f"[TREFFER] Lösche: {full_path}")
                
                try:
                    shutil.rmtree(full_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"   -> KONNTE NICHT LÖSCHEN: {e}")

    print("-" * 50)
    print(f"Fertig! Es wurden {deleted_count} Ordner vernichtet.")
    
    # Diagnose: Was ist jetzt noch im slideshow Ordner?
    slideshow_path = os.path.join(TARGET_ROOT, "slideshow")
    print(f"\nAktueller Inhalt von {slideshow_path}:")
    if os.path.exists(slideshow_path):
        for item in os.listdir(slideshow_path):
            print(f"  - {item}")
    else:
        print("  (Ordner slideshow existiert nicht!)")

    input("\nDrücke ENTER zum Beenden...")

if __name__ == "__main__":
    force_clean()