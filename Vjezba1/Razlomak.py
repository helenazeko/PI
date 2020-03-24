#1.1

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
        najmDjel = None

        if(self.brojnik <= self.nazivnik):
            manjiBr = self.brojnik
        else:
            manjiBr = self.nazivnik

        for i in range(2, int(manjiBr + 1)):
            if(self.brojnik % i == 0 and self.nazivnik % i == 0):
                najmDjel = i

        if(najmDjel == None):
            print("Razlomak se ne može skratiti.")
        else:
            self.nazivnik //= najmDjel
            self.brojnik //= najmDjel

#1.2

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

#1.3
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


print('*** test 1 ***')
r1 = Razlomak(12, 30)
print(r1.brojnik, r1.nazivnik)
r1.skrati
print(r1.brojnik, r1.nazivnik)

print('*** test 2 ***')
r1 = Razlomak(12, 30)
r2 = Razlomak(2, 5)
r3 = Razlomak(3, 6)
print(r1, r2, repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(3,4)+Razlomak(5,2))
print(Razlomak(1,3)-Razlomak(2,6))
print(Razlomak(2,8)*Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))

