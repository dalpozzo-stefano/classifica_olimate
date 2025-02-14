import requests
from bs4 import BeautifulSoup
import json
import time

# URL della classifica
URL = "https://gasmatematica.altervista.org/onehundredproblems/leaderboard.php?ID=12905"

# Utenti da includere nella classifica
utenti_filtrati = {"Giovanni Iotti", "Stefano Dal Pozzo", "NomeUtente3"}

def estrai_classifica():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Errore nel recupero della pagina")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    classifica = []

    tabella = soup.find("table")
    if not tabella:
        print("Tabella non trovata")
        return []

    righe = tabella.find_all("tr")[1:]  # Salta l'intestazione
    for riga in righe:
        colonne = riga.find_all("td")
        if len(colonne) < 3:
            continue

        posizione = colonne[0].text.strip()
        nome = colonne[1].text.strip()
        punteggio = colonne[2].text.strip()

        if nome in utenti_filtrati:
            classifica.append({"posizione": posizione, "nome": nome, "punteggio": punteggio})

    return classifica

def aggiorna_classifica():
    classifica_filtrata = estrai_classifica()
    with open("classifica.json", "w", encoding="utf-8") as f:
        json.dump(classifica_filtrata, f, indent=4, ensure_ascii=False)
    print("Classifica aggiornata!")

if __name__ == "__main__":
    aggiorna_classifica()
