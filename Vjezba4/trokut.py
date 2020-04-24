#4.1
from math import *
class Trokut(object):

    def __init__(self, a , b , c):
        if (a>=0 and b>=0 and c>=0 and a+b>c and a+c>b and b+c>a ):
            self.__stranice = [a,b,c]
        else:
            raise ValueError('Nije trokut')

    def __str__(self):
        return "trokut %s %s %s" % (self.__stranice[0], self.__stranice[1],self.__stranice[2])


    def __repr__(self):
        return "Trokut(%r ,  %r ,  %r)" % (self.__stranice[0], self.__stranice[1],self.__stranice[2])

#4.2

    def opseg(self):
        return self.__stranice[0] + self.__stranice[1] + self.__stranice[2]


    def povrsina(self):
        o = (self.__stranice[0] + self.__stranice[1]+ self.__stranice[2])
        s = o/2
        return sqrt((s-self.__stranice[0])*(s-self.__stranice[1])*(s-self.__stranice[2]))


#4.3

class JednakokracniTrokut(Trokut):
    def __init__(self, baza , krak):
        super(JednakokracniTrokut,self).__init__(baza, krak , krak)


class JednakostranicniTrokut(Trokut):
    def __init__(self,stranica):
        super(JednakostranicniTrokut,self).__init__(stranica, stranica, stranica)




print('*** test 1 ***')
lista_stranica = [(1,2,3),(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
    try:
       t = Trokut(*stranice)
       print(repr(t))
    except Exception as e:
       print(e, stranice)



print('*** test 2 ***')
lista_stranica = [(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
    t = Trokut(*stranice)
    print('%r ima opseg %.3f i povrsinu %.3f' % (t, t.opseg(), t.povrsina()))



print('*** test 3 ***')
trokuti = [Trokut(3,4,5),JednakokracniTrokut(3,4),JednakostranicniTrokut(5)]
for t in trokuti:
    print(t)


