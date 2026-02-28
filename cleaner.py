import ast
import os
import shutil

# Name deiner Datei
TARGET_FILE = "kassenprotokoll.py"

def remove_duplicate_methods(file_path):
    if not os.path.exists(file_path):
        print(f"Fehler: Datei '{file_path}' nicht gefunden.")
        return

    # 1. Backup erstellen
    backup_path = file_path + ".bak"
    shutil.copy2(file_path, backup_path)
    print(f"Backup erstellt: {backup_path}")

    # 2. Datei lesen
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()
        source_lines = source_code.splitlines()

    # 3. Code parsen (AST erstellen)
    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        print(f"Kritischer Fehler: Die Datei enthält Syntaxfehler und kann nicht geparst werden.\n{e}")
        return

    lines_to_remove = set()
    duplicates_found = 0

    # 4. Den Baum durchsuchen
    # Wir schauen uns Top-Level Funktionen und Methoden innerhalb von Klassen an
    
    # Hilfsfunktion zum Scannen eines Blocks (Module oder ClassDef)
    def scan_body(node, context_name="Global"):
        nonlocal duplicates_found
        seen_methods = set()
        
        # Wir iterieren durch alle Elemente im Body (Funktionen, Zuweisungen, etc.)
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                method_name = item.name
                
                if method_name in seen_methods:
                    # Duplikat gefunden!
                    duplicates_found += 1
                    print(f"Duplikat gefunden in '{context_name}': Methode '{method_name}' (Zeilen {item.lineno}-{item.end_lineno}) -> Wird entfernt.")
                    
                    # Markiere alle Zeilen dieser Funktion zum Löschen
                    # ast line numbers sind 1-basiert
                    for i in range(item.lineno, item.end_lineno + 1):
                        lines_to_remove.add(i)
                else:
                    seen_methods.add(method_name)

    # Globalen Scope scannen
    scan_body(tree)

    # Klassen scannen
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            scan_body(node, context_name=f"Class {node.name}")

    if duplicates_found == 0:
        print("Keine Duplikate gefunden. Die Datei ist sauber.")
        # Backup kann theoretisch gelöscht werden, aber sicherheitshalber lassen wir es.
        return

    # 5. Neue Datei schreiben (ohne die markierten Zeilen)
    new_lines = []
    # Zeilennummern in Editor sind 1-basiert, Liste ist 0-basiert
    for idx, line in enumerate(source_lines):
        lineno = idx + 1
        if lineno not in lines_to_remove:
            new_lines.append(line)

    # Ergebnis speichern
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    print("-" * 40)
    print(f"Fertig! {duplicates_found} Duplikate wurden entfernt.")
    print(f"Die bereinigte Datei wurde gespeichert unter: {file_path}")
    print("-" * 40)

if __name__ == "__main__":
    print("Start Code-Bereinigung...")
    remove_duplicate_methods(TARGET_FILE)