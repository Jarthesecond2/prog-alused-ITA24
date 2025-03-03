import csv
import sqlite3

def laadige_autod(fail):
    autod = []
    with open(fail, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for rida in reader:
            if 'mootori_võimsus' in rida and rida['mootori_võimsus'] and rida['mootori_võimsus'].isdigit():
                autod.append(rida)
    return autod

def arvuta_maks(auto):
    try:
        mootori_võimsus = int(auto['mootori_võimsus'])
        vanus = 2025 - int(auto['aasta'])
        maks = (mootori_võimsus * 0.1) + (vanus * 0.2)
        return round(maks, 2)
    except ValueError:
        return None


def loo_andmebaas():
    conn = sqlite3.connect('autod.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS autod
                 (nimi TEXT, aasta INTEGER, mootori_võimsus INTEGER, maks REAL)''')
    conn.commit()
    conn.close()

def salvesta_auto(auto):
    conn = sqlite3.connect('autod.db')
    c = conn.cursor()
    c.execute("INSERT INTO autod (nimi, aasta, mootori_võimsus, maks) VALUES (?, ?, ?, ?)",
              (auto['nimi'], auto['aasta'], auto['mootori_võimsus'], arvuta_maks(auto)))
    conn.commit()
    conn.close()

def kuvatulemused(autod):
    for auto in autod:
        print(f"{auto['nimi']}: Maks - {arvuta_maks(auto)} EUR")

def menüü():
    while True:
        print("\n1. Kuvada kõik autod ja nende maksud")
        print("2. Otsi auto nime järgi")
        print("3. Välju")
        valik = input("Valige toiming: ")

        if valik == '1':
            autod = laadige_autod('autod.csv')
            kuvatulemused(autod)
        elif valik == '2':
            nimi = input("Sisesta auto nimi: ")
            autod = laadige_autod('autod.csv')
            leitud = [auto for auto in autod if nimi.lower() in auto['nimi'].lower()]
            kuvatulemused(leitud)
        elif valik == '3':
            break
        else:
            print("Vale valik!")
