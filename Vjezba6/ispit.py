import json
import sqlite3

#6.1

class Ispit(dict):

    def dodaj(self, student, kolegij, ocjena):
        if student not in self:
            self[student] = {}
        self[student][kolegij] = ocjena

    def izbrisi(self, student, kolegij):
        if kolegij in self[student]:
            self[student].pop(kolegij)

    def promijeni(self, student, kolegij, ocjena):
        self[student][kolegij] = ocjena


    def spremi_datoteka(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding="utf8") as dat:
            for student, kolegiji_dict in self.items():
                for kolegiji, ocjena in kolegiji_dict.items():
                    dat.write("%s \t %s \t %s \n" % (student, kolegiji, str(ocjena)))



    @staticmethod
    def ucitaj_datoteku(naziv_datoteke):
        isp = Ispit()
        with open(naziv_datoteke, "r", encoding="utf8") as dat:
            for line in dat.readlines():
                info_string = line.split("\t")
                isp.dodaj(info_string[0].strip(), info_string[1].strip(), int(info_string[2].strip()))

        return isp


    def spremi_json(self, naziv_datoteke):
        with open(naziv_datoteke, "w", encoding="utf8") as dat:
            json.dump(self, dat)


    @staticmethod
    def ucitaj_json(naziv_datoteke):


        with open(naziv_datoteke, "r", encoding="utf8") as dat:
           isp = Ispit(json.load(dat))
           return isp


isp = Ispit()
isp.dodaj("Ante Antić", "Linearna algebra", 5)
isp.dodaj("Ante Antić", "Programiranje 1", 4)
isp.dodaj("Marija Marijić", "Linearna algebra", 4)
isp.dodaj("Marija Marijić", "Matematička analiza", 5)

isp.spremi_datoteka("ispiti.txt")
print(open("ispiti.txt", encoding="utf8").read())

isp = Ispit.ucitaj_datoteku("ispiti.txt")
print(isp)



isp.spremi_json("ispiti.json")
print(open("ispiti.json", encoding="utf8").read())
Ispit.ucitaj_json("ispiti.json")
print(isp)





