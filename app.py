import datetime

pajamos = []
islaidos = []

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
            ivesta_data = input("Įveskite datą > ")
            suma = float(input("Įveskite norimas pajamas > "))
            rusis = input("Įveskite pajamų rūšį > ")
            pajamos.append((ivesta_data, suma, rusis))
            print("Pajamos įvestos!\n")
        except ValueError:
            print("Klaida, įveskite teisingą sumą. \n")

    elif pasirinkimas == "2":
        try:
            ivesta_data = input("Įveskite datą > ")
            suma = float(input("Įveskite norimas išlaidas > "))
            rusis = input("Įveskite išlaidų rūšį > ")
            islaidos.append((ivesta_data, suma, rusis))
            print("Išlaidos įvestos!\n")
        except ValueError:
            print("Klaida, įveskite teisingą sumą. \n")

    elif pasirinkimas == "3":
        if not pajamos:
            print("Pajamos dar neįvestos")
        else:
            print("\n ---- Pajamų sąrašas ----")
            for ivesta_data, suma, rusis in pajamos:
                print(f"<<{ivesta_data}>> {rusis}: {suma} EUR")
            print()

    elif pasirinkimas == "4":
        if not islaidos:
            print("Išlaidos dar nepridėtos")
        else:
            print("\n ---- Išlaidų sarašas ----")
            for ivesta_data, suma, rusis in islaidos:
                print(f"<<{ivesta_data}>> {rusis}: {suma} EUR")
            print()

    elif pasirinkimas == "5":
        pajamu_suma = sum([suma for suma, _ in pajamos])
        islaidu_suma = sum([suma for suma, _ in islaidos])
        balansas = pajamu_suma - islaidu_suma
        print("\n ---- Statistika ----")
        print(f"Pajamos: {pajamu_suma} EUR")
        print(f"Išlaidos: {islaidu_suma} EUR")
        print(f"Balansas: {balansas} EUR \n")
        print()











