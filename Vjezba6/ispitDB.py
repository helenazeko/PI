import sqlite3
from vjezba6.ispit import ispit


class IspitiDB():
    def __init__(self, baza):
        self.conn = sqlite3.Connection(baza)
        self.cur = self.conn.cursor()
        self.cur.executescript("""
                    DROP TABLE IF EXISTS ispiti;
                    DROP TABLE IF EXISTS kolegiji;
                    DROP TABLE IF EXISTS studenti;

                    CREATE TABLE studenti (
                        student_id integer PRIMARY KEY,
                        ime_prezime text NOT NULL UNIQUE);

                    CREATE TABLE kolegiji (
                        kolegiji_id integer PRIMARY KEY,
                        naziv text NOT NULL UNIQUE);

                    CREATE TABLE ispiti (
                        student_id integer,
                        kolegiji_id integer,
                        ocjena integer NOT NULL,
                        PRIMARY KEY (student_id, kolegiji_id),
                        FOREIGN KEY (student_id) REFERENCES studenti (student_id),
                        FOREIGN KEY (kolegiji_id) REFERENCES kolegiji (kolegiji_id));
                    """)

    def vrati_kolegiji_id(self, naziv):
        self.cur.execute("""SELECT kolegiji_id FROM kolegiji WHERE naziv = ?""",(naziv,))
        row = self.cur.fetchone()
        if row:
            return row[0]

    def dodaj_kolegiji(self, naziv):
        self.cur.execute("""INSERT INTO kolegiji (naziv) VALUES (?)""",(naziv,))
        self.conn.commit()
        return self.cur.lastrowid

    def vrati_student_id(self, ime_prezime):
        self.cur.execute("SELECT student_id FROM studenti WHERE ime_prezime LIKE (?)", (ime_prezime,))
        row = self.cur.fetchone()
        if row:
            return row[0]

    def dodaj_student(self, ime_prezime):
        self.cur.execute("INSERT INTO studenti (ime_prezime) VALUES (?)", (ime_prezime,))
        self.conn.commit()
        return self.cur.lastrowid

    def promijeni_student(self, current_ime_prezime, new_ime_prezime):
        stud_id = self.vrati_student_id(current_ime_prezime)

        if stud_id:
            self.cur.execute("UPDATE studenti SET ime_prezime = (?) WHERE student_id LIKE (?)", (new_ime_prezime, stud_id))
            self.conn.commit()
            return self.cur.lastrowid
        else:
            return None

    def izbrisi_student(self, ime_prezime):
        stud_id = self.vrati_student_id(ime_prezime)

        if stud_id:
            self.cur.execute("DELETE FROM studenti WHERE student_id LIKE (?)", (stud_id,))
            self.conn.commit()

    def ispitaj(self, student, kolegiji, ocjena = None):
        self.cur.execute("SELECT 1 FROM ispiti WHERE student_id = (?) AND kolegiji_id = (?)", (self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji)))
        row = self.cur.fetchone()

        if ocjena == None:
            if row:
                self.cur.execute("DELETE FROM ispiti WHERE student_id = (?) AND kolegiji_id = (?)", (self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji)))
                self.conn.commit()
        else:
            if row:
                self.cur.execute("UPDATE ispiti SET ocjena = (?) WHERE student_id = (?) AND kolegiji_id = (?)", (ocjena, self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji)))
                self.conn.commit()
            else:
                self.cur.execute("INSERT INTO ispiti (student_id, kolegiji_id, ocjena) VALUES (?, ?, ?)", (self.vrati_student_id(student), self.vrati_kolegiji_id(kolegiji), ocjena))
                self.conn.commit()

    def svi_ispiti(self):
        self.cur.execute("""
            SELECT s.ime_prezime, k.naziv, i.ocjena
            FROM studenti AS s
            JOIN ispiti AS i ON s.student_id = i.student_id
            JOIN kolegiji AS k ON k.kolegiji_id = i.kolegiji_id
        """)

        isp = Ispit()
        for counter in self.cur.fetchall():
            isp.dodaj(counter[0], counter[1], counter[2])

        return isp



print('*** TEST SQLite studenti ***')
db = IspitiDB("ispiti.sqlite")
print(db.cur.execute("SELECT * FROM studenti").fetchall())

db.dodaj_student("Ante Antić")
db.dodaj_student("Ana Anić")
db.dodaj_student("Pero Perić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())
print(db.vrati_student_id("Pero Perić"))
print(db.vrati_student_id("Marija Marijić"))

db.izbrisi_student("Pero Perić")
db.promijeni_student("Ana Anić","Marija Marijić")
print(db.cur.execute("SELECT * FROM studenti").fetchall())


print('*** TEST SQLite ispiti ***')
db = IspitiDB("ispiti.sqlite")
db.dodaj_student("Ante Antić")
db.dodaj_student("Marija Marijić")
db.dodaj_kolegiji("Linearna algebra")
db.dodaj_kolegiji("Programiranje 1")
db.dodaj_kolegiji("Matematička analiza")
db.ispitaj("Ante Antić", "Linearna algebra", 5)
db.ispitaj("Ante Antić", "Linearna algebra", 3)
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra",4)
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra")
print(db.svi_ispiti())
db.ispitaj("Ante Antić","Linearna algebra",5)
db.ispitaj("Marija Marijić","Programiranje 1",5)
db.ispitaj("Marija Marijić","Matematička analiza",4)
print(db.svi_ispiti())

