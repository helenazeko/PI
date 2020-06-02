from pprint import pprint

class Kvadrat():



    def __init__(self, broj = 0):
        self.__broj = broj
        self.__otkriven = False
        self.__oznaka = False

    def otkrij(self):
        if self.__otkriven == False:
            self.__otkriven = True

    def oznaci(self):
        if self.__oznaka == False:
            self.__oznaka = True
        else:
            self.__oznaka = False

    @property
    def jeMina(self):
        if self.__broj == -1:
            return True
        return False

    @property
    def jeBroj(self):
        if self.__broj > 0:
            return True
        return False

    @property
    def broj(self):
        return self.__broj

    @property
    def jePrazan(self):
        if self.__broj == 0:
            return True
        return False



    def __str__(self):
        if self.__otkriven == False:
            return "."
        elif self.__oznaka == True:
            return "?"
        elif self.__otkriven == True and self.__broj == -1:
            return "x"
        elif self.__otkriven == True and self.__broj > 0:
            return str(self.__broj)
        elif self.__otkriven == True and self.__broj == 0:
            return " "




