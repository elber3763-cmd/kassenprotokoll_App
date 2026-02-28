import os
import shutil

def clean_pycache(root_dir):
    print(f"Starte Bereinigung in: {root_dir}")
    count = 0
    
    # Durchlaufe alle Unterordner
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Wir erstellen eine Kopie der Liste, damit wir sie während des Durchlaufs ändern können
        for dirname in dirnames[:]:
            # Prüfen, ob "pycache" im Namen vorkommt
            if "__pycache__" in dirname:
                full_path = os.path.join(dirpath, dirname)
                try:
                    print(f"Lösche: {full_path}")
                    shutil.rmtree(full_path) # Löscht den Ordner und den Inhalt
                    dirnames.remove(dirname) # Verhindert, dass os.walk in den gelöschten Ordner geht
                    count += 1
                except Exception as e:
                    print(f"Fehler beim Löschen von {full_path}: {e}")

    print("-" * 30)
    print(f"Fertig! Es wurden {count} Ordner gelöscht.")
    print("-" * 30)
    input("Drücke ENTER zum Beenden...")

if __name__ == "__main__":
    # Das Skript führt sich im aktuellen Ordner aus
    current_directory = os.getcwd()
    clean_pycache(current_directory)