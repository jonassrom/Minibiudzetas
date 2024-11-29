

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
        break

    if pasirinkimas == "1":
        while True:
           suma = input("Įveskite norimas pajamas > ")


