# Aufgabe 1
# erstelle mit einer List Comprehension 3 Listen mit einem Leerzeichen in einer Liste mit dem Namen Spielfeld
# gib deine List Comprehension aus
# die Ausgabe sollte so aussehen: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Aufgabe 2
# 2.1 Suche im Internet nach der Methode .join() und erkläre im Detail was diese macht

#    In Python wird die Methode .join() häufig verwendet, 
#    um Elemente einer iterierbaren Sammlung (wie Listen oder Tupel) 
#    zu einem einzigen String zu verbinden, wobei ein bestimmter Trennstring zwischen den Elementen eingefügt wird.

#    separator = "Trennzeichen"  # Zum Beispiel: ", ", " - ", " | "
#    result = separator.join(iterable) 

#    zahlen = ["1", "2", "3", "4", "5"]
#    ergebnis = " - ".join(zahlen)
#    print(ergebnis)  # Ausgabe: 1 - 2 - 3 - 4 - 5

# 2.2 Schreibe eine Funktion mit dem Namen zeichne_spielfeld() mit einer for Schleife, die jede Liste deiner List Comprehension untereinander ausgibt
# 2.3 Benutze die join Methode, um die Listen mit einem " | " Zeichen miteinander zu verbinden und gebe sie in der Console aus.
# 2.4 füge jeder Liste in einer Reihe einen Boden mit "-" hinzu und gebe dein Spielfeld in der Console aus. (Tipp: 9 Trennstriche sehen gut und symmetrisch aus)
# Das Ergebnis sollte etwa wie folgt aussehen:
#
#  |   |
#---------
#  |   |
#---------
#  |   |
#---------

# Aufgabe 3
# 3.1 Baue eine Hauptfunktion mit dem Namen starte_spiel(), kopiere deine List Comprehension mit deinem
#     Spielfeld in die Funktion, so das dein Spielfeld bei dem Aufruf der Funktion erstellt wird
# 3.2 Definiere eine Variable mit dem Namen aktueller_spieler = 'X' in deiner Funkion
# 3.3 Baue eine While Schleife, in deiner starte_spiel() Funktion, die bei dem Start der Schleife
#     deine Funktion zeichne_spielfeld aufruft. (TIPP: Vergiss nicht die Parameterübergabe)
# 3.4 Fordere innerhalb deiner While Schleife eine Eingabe an, welche die Zeile mit einer Zahl empfängt und speichere den Wert der
#     Eingabe in der Variable zeile. Dieser Wert wird später auf den Index deines Feldes zugreifen
# 3.5 Fordere innerhalb deiner While Schleife eine weitere Eingabe an, welche die Spalte mit einem Zahlenwert empfängt, die später dem Index der
#     Spalte zugewiesen wird und speichere den Wert der Eingabe in einer Variablen mit dem Namen spalte

# Aufgabe 4
# Du hast ein 2 Dimensionales Spielfeld gebaut, auf dessen Felder du zugreifen kannst. Finde heraus, wie du das Zeichen deines aktuellen Spielers
# auf die Felder der getätigten Eingabe setzen kannst und erweitere deine Funktion starte_spiel() mit der Zuweisung X auf die Eingabe des Spielers

# Aufgabe 5
# Wechsle den aktuellen Spieler in deiner While Schleife von "X" auf "O" und falls dieser Spieler schon auf "O" stehen sollte, wechsle ihn wieder zu "X"
# Teste mal aus, ob es schon funktioniert

# Aufgabe 6
# Atme mal tief durch, trink nen Schluck und wenn du fertig bist, zeige mit einem print Befehl an, welcher Spieler grade bei dem neuen Schleifendurchlauf an
# der Reihe ist

# Aufgbe 7
# Begründe warum du die Zahlen 0 - 2 eingeben musst.
 
# Aufgabe 8
# Was wäre eine Lösung, wenn du die Zahlen 1 - 3 eingeben möchtest, weil sich diese Eingabe intuitiver anfühlt?
# Welche Problematik tritt auf und wie können wir diese beheben und umsetzen ?


# Teil 2

# Aufgabe 1
# Baue eine Funktion, die prüft, ob das Spielfeld voll ist. Falls ja, beende das Spiel.

# Aufgabe 1.2
# Überlege wie du das Problem beheben kannst, das dein Spielfeld auch den letzten Spielzug anzeigt.

# Aufgabe 2
# Fast geschafft!!!! Engegner!!! XD
# Aufgabe 2.1
# Baue eine Funktion mit dem Namen ueberpruefe_gewinner(), die bei jedem Spielzug überprüft, ob alle Reihen das jeweilige Zeichen 3 mal enthalten.
# (Tipp: Denke an die Parameter)
# Aufgabe 2.2
# erweitere deine Funktion ueberpruefe_gewinner() mit der gleichen Kontrolle über jede Spalte
# Aufgabe 2.3
# Überprüfe jetzt noch die Diagonalen Felder

# Aufgabe 3
# Fange einen Fehler ab, falls ein Spieler etwas anderes als eine Zahl als Eingabe tätigt. Der Spieler soll darauf hin seinen Spielzug wiederholen
# Aufgabe 3.2
# Überprüfe ob die Eingabe in einem Gültigen Feldbereich liegt. Falls ein Feld besetzt sein sollte, gib aus, das der Zug ungültig ist und der Spieler
# soll seinen Spielzug wiederholen.


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