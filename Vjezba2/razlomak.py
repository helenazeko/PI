class Razlomak(object):

 '''Klasa razlomak'''
 def __init__(self, brojnik, nazivnik = 1):
     if nazivnik == 0: raise Exception('Nazivnik ne moze biti 0')
     self._brojnik = brojnik
     self._nazivnik = nazivnik


 def __str__(self):
   return '%d|%d' % (self._brojnik, self._nazivnik)


 @staticmethod
 def inverz(self):
    return Razlomak(self._nazivnik, self._brojnik)

 @staticmethod
 def stvori(broj:float):
    string = str(broj)
    if not '.' in string:
        return 0

    else:
        brDecimalnihMjesta = len(string) - string.index('.') - 1

        br = "1"

        for i in range (brDecimalnihMjesta):
            br = br + "0"

        return Razlomak(broj * int (br), int(br))



print('*** test1 ***')
r1 = Razlomak(314,100)
r2 = Razlomak.inverz(r1)
print(r1,r2,r1)

print('*** test2 ***')
r1 = Razlomak.stvori(3.14)
print(r1)
r2 = Razlomak.stvori(0.006021)
print(r2)
r3 = Razlomak.stvori(-75.204)
print(r3)