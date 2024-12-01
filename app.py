# from funkcijos import issaugoti_duomenis, uzkrauti_duomenis
import datetime
import pickle
import os

pajamos = []
islaidos = []


def issaugoti_duomenis():
    try:
        with open('biudzetas.pkl', 'wb') as file:
            # noinspection PyTypeChecker
            pickle.dump([pajamos, islaidos], file)
        print("Duomenys išsaugoti sėkmingai.\n")
    except Exception as e:
        print(f"Klaida išsaugant duomenis: {e}")


def uzkrauti_duomenis():
    global pajamos, islaidos
    if os.path.exists('biudzetas.pkl'):
        try:
            with open('biudzetas.pkl', 'rb') as file:
                pajamos, islaidos = pickle.load(file)
            print("Duomenys užkrauti sėkmingai.\n")
        except Exception as e:
            print(f"Klaida užkraunant duomenis: {e}")
    else:
        print("Nėra rastas duomenų failas.\n")


uzkrauti_duomenis()

while True:
    print("1. Įvesti pajamas\n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "q - Išeiti\n")

    pasirinkimas = input("Pasrinkite norimą opciją > ")

    if pasirinkimas == "q":
        print("Išėjote iš meniu")
        break

    elif pasirinkimas == "1":
        try:
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            suma = float(input("Įveskite norimas pajamas > "))
            rusis = input("Įveskite pajamų rūšį > ")
            pajamos.append([data, suma, rusis])
            print("Pajamos įvestos!\n")
            issaugoti_duomenis()
        except ValueError:
            print("Klaida, įveskite teisingą sumą. \n")

    elif pasirinkimas == "2":
        try:
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            suma = float(input("Įveskite norimas išlaidas > "))
            rusis = input("Įveskite išlaidų rūšį > ")
            islaidos.append([data, suma, rusis])
            print("Išlaidos įvestos!\n")
            issaugoti_duomenis()
        except ValueError:
            print("Klaida, įveskite teisingą sumą. \n")

    elif pasirinkimas == "3":
        if pajamos:
            print("\n ---- Pajamų sąrašas ----")
            for pajamos_eilute in pajamos:
                print(f"<{pajamos_eilute[0]}> {pajamos_eilute[1]}: {pajamos_eilute[2]} EUR")
        else:
            print("Pajamos dar neįvestos")
            print()

    elif pasirinkimas == "4":
        if islaidos:
            print("\n ---- Išlaidų sarašas ----")
            for islaidos_eilute in islaidos:
                print(f"<{islaidos_eilute[0]}> {islaidos_eilute[1]}: {islaidos_eilute[2]} EUR")
            else:
                print("Išlaidos dar nepridėtos")
                print()

    elif pasirinkimas == "5":
        pajamu_suma = sum([eilute[1] for eilute in pajamos])
        islaidu_suma = sum([eilute[1] for eilute in islaidos])
        balansas = pajamu_suma - islaidu_suma
        print("\n ---- Statistika ----")
        print(f"Pajamos: {pajamu_suma} EUR")
        print(f"Išlaidos: {islaidu_suma} EUR")
        print(f"Balansas: {balansas} EUR \n")
