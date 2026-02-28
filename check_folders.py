import os

def list_all_folders(root_dir):
    print(f"Untersuche Verzeichnis: {root_dir}")
    print("-" * 40)
    
    found_any = False
    
    # Durchlaufe alle Unterordner
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            # Wir zeigen ALLE Ordner an, um zu sehen, wie sie heißen
            full_path = os.path.join(dirpath, dirname)
            print(f"Gefunden: {dirname}")
            print(f"   Pfad: {full_path}")
            
            if "__pycache__" in dirname:
                print("   >>> TREFFER! Das Skript müsste diesen löschen.")
            
            found_any = True
            
    if not found_any:
        print("Keine Unterordner gefunden!")

    print("-" * 40)
    input("Drücke ENTER zum Beenden...")

if __name__ == "__main__":
    current_directory = os.getcwd()
    list_all_folders(current_directory)