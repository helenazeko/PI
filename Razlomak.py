
class Razlomak(object):

    def __init__(self,brojnik,nazivnik):
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    @property
    def brojnik(self):
        return self._brojnik

    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value

    @property
    def nazivnik(self):
        return self._nazivnik

    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik = value


    @property
    def skrati(self):
        najmanjiDjeljitelj = None

        if(self.brojnik <= self.nazivnik):
            manjiBroj = self.brojnik
        else:
            manjiBroj = self.nazivnik

        for djeljitelj in range(2, int(manjiBroj + 1)):
            if(self.brojnik % djeljitelj == 0 and self.nazivnik % djeljitelj == 0):
                najmanjiDjeljitelj = djeljitelj

        if(najmanjiDjeljitelj == None):
            print("Razlomak se ne može skratiti.")
        else:
            self.nazivnik //= najmanjiDjeljitelj
            self.brojnik //= najmanjiDjeljitelj
            print("Razlomak se može skratiti sa brojem", najmanjiDjeljitelj, "te razlomak sada izgleda:", repr(self))

    def __repr__(self):
        return "Razlomak(" + repr(self.brojnik) + ", " + repr(self.nazivnik) + ")"

    def __str__(self):
        return str(self.brojnik) + "|" + str(self.nazivnik)

    def __eq__(self, other):
        return (self.brojnik / self.nazivnik) == (other.brojnik / other.nazivnik)

    def __ge__(self, other):
        return (self.brojnik / self.nazivnik) >= (other.brojnik / other.nazivnik)

    def __lt__(self, other):
        return (self.brojnik / self.nazivnik) < (other.brojnik / other.nazivnik)

    def __add__(self, other):
        brojnik = (self.brojnik * other.nazivnik) + (other.brojnik * self.nazivnik)
        nazivnik = self.nazivnik * other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))

    def __sub__(self, other):
        brojnik = (self.brojnik * other.nazivnik) - (other.brojnik * self.nazivnik)
        nazivnik = self.nazivnik * other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))

    def __mul__(self, other):
        brojnik = self.brojnik * other.brojnik
        nazivnik = self.nazivnik * other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))

    def __truediv__(self, other):
        brojnik = self.brojnik / other.brojnik
        nazivnik = self.nazivnik / other.nazivnik

        return repr(Razlomak(brojnik, nazivnik))



