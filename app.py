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
        if not pajamos:
            print("Pajamos dar neįvestos")
        else:
            print("\n ---- Pajamų sąrašas ----")
            for data, suma, rusis in pajamos:
                print(f"<{data}> {rusis}: {suma} EUR")

            print()

    elif pasirinkimas == "4":
        if not islaidos:
            print("Išlaidos dar nepridėtos")
        else:
            print("\n ---- Išlaidų sarašas ----")
            for data, suma, rusis in islaidos:
                print(f"<{data}> {rusis}: {suma} EUR")
            print()

    elif pasirinkimas == "5":
            pajamu_suma = sum([suma for suma, _ in pajamos])
            islaidu_suma = sum([suma for suma, _ in islaidos])
            balansas = pajamu_suma - islaidu_suma
            print("\n ---- Statistika ----")
            print(f"Pajamos: {pajamu_suma} EUR")
            print(f"Išlaidos: {islaidu_suma} EUR")
            print(f"Balansas: {balansas} EUR \n")


# if __name__ == "__main__":
    uzkrauti_duomenis()




