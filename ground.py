import time

print("""
 __           .__   __         .__          __
|  | _______  |  | |  | ____ __|  | _____ _/  |_  ___________
|  |/ /\__  \ |  | |  |/ /  |  \  | \__  \   __\/  _ \_  __  \|
|    <  / __ \|  |_|    <|  |  /  |__/ __ \|  | (  <_> )  | \/
|__|_ \(____  /____/__|_ \____/|____(____  /__|  \____/|__|
     \/     \/          \/               \/

     """)

print("""legenda działań:
+ dodawanie
- odejmowanie
* mnożenie
/ dzielenie
""")

def kalkulacja():
    x = int(input("""
Pierwsza liczba > """))

    y = input("Działanie > ")

    z = int(input("Druga liczba > "))

    if y == "*":
        print("Wynik =", x * z)
    elif y == "+":
        print("Wynik =", x+z)
    elif y == "-":
        print("Wynik =", x-z)
    elif y == "/":
        print("Wynik =", x/z)
    else:
        print("Niepoprawny znak. Spróbuj jescze raz")
        kalkulacja()
kalkulacja()
def again():
    while True:
        znowu = input("""
Obczliczyć jeszcze raz? (y/n) :""")
        if znowu == "y":
            kalkulacja()
        elif znowu == "n":
            print("Do zobaczenia")
            time.sleep(1)
            break
        else:
            again()


again()
