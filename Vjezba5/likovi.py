#5.1

class Kruznica(object):
    def __init__(self, radijus):
        self.__radijus = radijus


    @property
    def radijus(self):
        return self.__radijus

    @radijus.setter
    def radijus(self, radijus):
        self.radijus = radijus

    def __str__(self):
        return 'Kruznica radijusa r "%.2f"' % self.__radijus



class Kvadrat(object):
    def __init__(self, stranica):
        self.__stranica = stranica

    @property
    def duljina_stranice(self):
        return self.__duljina_stranice

    @duljina_stranice.setter
    def kvadrat(self, duljina_stranice):
        self.__duljina_stranice = duljina_stranice

    def __str__(self):
        return 'Kvadrat stranice s "%.2f"' % self.__stranica


if __name__ == "__main__":
    print('*** test likovi ***')
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)