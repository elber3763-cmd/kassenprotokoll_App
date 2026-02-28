import os
import shutil

# Der Pfad, wo das Chaos vermutet wird
TARGET_DIR = r"O:\kassenprotokoll_App\images\slideshow"

def clean_slideshow_mess():
    print(f"Ziele auf Ordner: {TARGET_DIR}")
    print("-" * 40)

    if not os.path.exists(TARGET_DIR):
        print("FEHLER: Der Ordner 'images/slideshow' wurde nicht gefunden!")
        input("Drücke Enter...")
        return

    count = 0
    
    # Wir schauen uns direkt den Inhalt dieses Ordners an
    try:
        items = os.listdir(TARGET_DIR)
        for item_name in items:
            full_path = os.path.join(TARGET_DIR, item_name)
            
            # Prüfen: Ist es ein Ordner? UND enthält der Name "pycache"?
            # Das fängt "__pycache__", "pycache - Kopie", etc. ab.
            if os.path.isdir(full_path) and "pycache" in item_name.lower():
                print(f"Lösche Ordner: {item_name}")
                try:
                    shutil.rmtree(full_path)
                    count += 1
                except Exception as e:
                    print(f"  FEHLER beim Löschen von {item_name}: {e}")
            
            # Optional: Falls es Dateien sind (keine Ordner), die so heißen:
            elif os.path.isfile(full_path) and "pycache" in item_name.lower():
                 print(f"Lösche Datei: {item_name}")
                 os.remove(full_path)
                 count += 1

    except Exception as e:
        print(f"Allgemeiner Fehler: {e}")

    print("-" * 40)
    print(f"Fertig! Es wurden {count} Elemente aus der Slideshow entfernt.")
    input("Drücke ENTER zum Beenden...")

if __name__ == "__main__":
    clean_slideshow_mess()