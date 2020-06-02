from vjezba_10.slagalica.Ploca import Ploca

class PrikazIgre():



    def izaberiVelicinu(self, velicine: list):
        slagalica = {}

        print("Izaberi velicinu:")

        for counter in range(len(velicine)):
            slagalica[str(counter + 1)] = velicine[counter]

            print(counter + 1, ". velicina ", velicine[counter][0], "x", velicine[counter][1], sep="")

        while True:
            odabranaVelicina = str(input("\nOdaberite jednu od navedenih tezina: "))

            if odabranaVelicina in slagalica:
                print("Odabrana je velicina", odabranaVelicina)
                return odabranaVelicina
            else:
                print("*" * 10, "NEVALJANA VELICINA", "*" * 10)



    def prikaziPlocu(self, ploca: Ploca):
        print(ploca)




    def unesiPolje(self, brojPolja):
        print("\n" + "*" * 5, "PRAVILO", "*" * 5)
        print("0 < ", "broj koji Vi unosite < ", brojPolja, sep = "")

        while True:
            unosPolje = input("Unesite broj polja: ")

            try:
                unosPolje = int(unosPolje)
            except:
                print("*" * 10, "NEVALJANO POLJE", "*" * 10)
                continue

            if unosPolje > 0 and unosPolje < brojPolja:
                return unosPolje
            else:
                print("*" * 10, "NEVALJANO POLJE", "*" * 10)


