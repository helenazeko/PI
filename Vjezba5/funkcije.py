#5.2

from likovi import *
from math import pi

def opseg(lik):
    if isinstance (lik, Kvadrat) == True:
        return 4 * lik.stranica

def povrsina(lik):
    if isinstance (lik, Kvadrat) == True:
        return lik.stranica * lik.stranica


def opseg(lik):
    if isinstance (lik, Kruznica) == True:
        return (2 * lik.radijus) * pi

def povrsina(lik):
    if isinstance (lik, Kruznica) == True:
        return (lik.radijus * lik.radijus) * pi


if __name__ == "__main__":
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)


