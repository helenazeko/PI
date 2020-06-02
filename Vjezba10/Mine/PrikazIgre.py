from vjezba_10.Mine.Polje import Polje

class PrikazIgre():




    def izaberiTezinu(self, tezina: list):
        tezine = {}

        print("Izaberi tezinu:")

        for counter in range(len(tezina)):
            tezine[str(counter + 1)] = tezina[counter]

            print(counter + 1, ". velicina ", tezina[counter][0], ", broj mina ",tezina[counter][1], sep = "")

        while True:
            odabranaTezina = str(input("\nOdaberite jednu od navedenih tezina: "))


            if odabranaTezina in tezine:
                print("Odabrana je težina", odabranaTezina)
                return odabranaTezina
            else:
                print("*" * 10, "NEVALJANA TEŽINA", "*" * 10)




    def prikaziPolje(self, polje: Polje):
            print(polje)





    def unesiAkciju(self, velicina):
        print("\n", "*" * 10, "PRAVILO UNOSA", "*" * 10 ,"\nAko želite otkriti polje unesite koordinate polja (npr [2 3] ili [2,3]) kojeg želite otkriti\nAko želite označiti polje ispred unosa koordinata dodajte znak '?' (npr [?2 3], [? 2,3] ili [? 2 3])")
        while True:
            koordinata = input("Unesite koordinate: ")
            koordinateTrimed = ""
            operacija = ""

            if "?" in koordinata:
                operacija = "oznaci"
                koordinateTrimed = koordinata.replace("?", "").strip()
            else:
                operacija = "otkrij"
                koordinateTrimed = koordinata

            if "," in koordinata:
                koordinateTrimed = koordinateTrimed.split(",")
            else:
                koordinateTrimed = koordinateTrimed.split(" ")

            try:
                koordinateTrimed = [int(koordinateTrimed[0]), int(koordinateTrimed[1])]
            except:
                continue

            if (koordinateTrimed[0] > 0 and koordinateTrimed[0] <= velicina) and (koordinateTrimed[1] > 0 and koordinateTrimed[1] <= velicina):
                return (operacija, koordinateTrimed[0], koordinateTrimed[1])
