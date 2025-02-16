# List Comprehension, um ein Spielfeld zu erstellen
spielfeld = [[" " for _ in range(3)] for _ in range(3)]

def zeichne_spielfeld(spielfeld):
    for reihe in spielfeld:
        print(" | ".join(reihe))
        print("-"*9)


def spielfeld_voll(spielfeld):
    for reihe in spielfeld:
        if " " in reihe:
            return False
    return True


def ueberpruefe_gewinner(spielfeld, zeichen):
    # Überprüfe Reihen
    for reihe in spielfeld:
        if reihe.count(zeichen) == 3:
            return True
        
    # Überprüfe Spalten
    for spalte in range(3):
        if (spielfeld[0][spalte] == zeichen and
            spielfeld[1][spalte] == zeichen and
            spielfeld[2][spalte] == zeichen):
            return True
        
    # Überprüfe Diagonalen   
    if (spielfeld[0][0] == zeichen and spielfeld[1][1] == zeichen and spielfeld[2][2] == zeichen) or \
       (spielfeld[0][2] == zeichen and spielfeld[1][1] == zeichen and spielfeld[2][0] == zeichen):
        return True

    return False

def starte_spiel():
    spielfeld = [[" " for _ in range(3)] for _ in range(3)]
    aktueller_spieler = "X"
    
    while True:
        
        zeichne_spielfeld(spielfeld)
        print(f"Spieler {aktueller_spieler} an der Reihe ")
        
        # Fehlerbehandlung für ungültige Eingaben
        try:
            # Zeile und Spalte eingeben
            zeile = int(input("Bitte Zeile eingeben 1 - 3 ")) - 1
            spalte = int(input("Bitte spalte eingeben 1 - 3 ")) - 1
        
            # Überprüfe, ob die Eingaben im gültigen Bereich liegen
            if zeile not in range(3) or spalte not in range(3):
                print("Ungültiger Bereich! Bitte Zahlen von 1 bis 3 eingeben.")
                continue
            
            # Stelle sicher, dass das gewählte Feld leer ist
            if spielfeld[zeile][spalte] != " ":
                print("Das Feld ist bereits belegt, bitte wähle ein anderes.")
                continue
            
        except (ValueError):
            print("Ungültige Eingabe! Bitte nur Zahlen von 1 bis 3 eingeben.")
            continue
        
        # Setze das Zeichen auf das Spielfeld
        spielfeld[zeile][spalte] = aktueller_spieler
        
        # Überprüfe, ob ein Spieler gewonnen hat
        if ueberpruefe_gewinner(spielfeld, aktueller_spieler):
            zeichne_spielfeld(spielfeld)
            print(f"Spieler {aktueller_spieler} hat gewonnen!")
            break
        
        # Überprüfe, ob das Spielfeld voll ist
        if spielfeld_voll(spielfeld):
            zeichne_spielfeld(spielfeld)
            print("Das Spielfeld ist voll ")
            break

        if aktueller_spieler == "X":
                aktueller_spieler = "O"
        else:
                aktueller_spieler = "X"

        


starte_spiel()