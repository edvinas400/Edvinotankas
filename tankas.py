import random
import pickle


class Tankas():
    def __init__(self, x=0, y=0, kryptis="Siaure", suviai={"Siaure: ": 0, "Rytai: ": 0, "Pietus: ": 0, "Vakarai: ": 0},
                 taskai=100, score=0):
        self.x = x
        self.y = y
        self.taskai = taskai
        self.score = score
        self.kryptis = kryptis
        self.suviai = suviai
        self.taikinys()
        try:
            with open("rezultatai.pkl", "rb") as file:
                self.highscores = pickle.load(file)
        except:
            self.highscores = []
        self.info()

    def taskusekimas(self):
        if self.taskai <= 0:
            name = input(f"Zaidimas baigtas, jusu rezultatas: {self.score}, iveskite savo varda: ")
            with open("rezultatai.pkl", "wb") as file:
                add = f"{name}: {self.score}"
                self.highscores.append(add)
                pickle.dump(self.highscores, file)
            exit()

    def pirmyn(self):
        self.y += 1
        self.kryptis = "Siaure"
        self.taskai -= 10
        self.taskusekimas()
        self.info()

    def kairen(self):
        self.x -= 1
        self.kryptis = "Vakarai"
        self.taskai -= 10
        self.taskusekimas()
        self.info()

    def atgal(self):
        self.y -= 1
        self.kryptis = "Pietus"
        self.taskai -= 10
        self.taskusekimas()
        self.info()

    def desinen(self):
        self.x += 1
        self.kryptis = "Rytai"
        self.taskai -= 10
        self.taskusekimas()
        self.info()

    def suvis(self):
        if self.kryptis == "Siaure":
            self.suviai["Siaure: "] += 1
        if self.kryptis == "Rytai":
            self.suviai["Rytai: "] += 1
        if self.kryptis == "Pietus":
            self.suviai["Pietus: "] += 1
        if self.kryptis == "Vakarai":
            self.suviai["Vakarai: "] += 1
        print(self.ar_pataike())
        if self.ar_pataike() == "Pataikyta!":
            self.taskai += 50
            self.score += 1
            self.taikinys()
            print(f"Sukurtas naujas taikinys {self.taik}")
        self.info()

    def info(self):
        print(f"Tanko kryptis: {self.kryptis}")
        print(f"Tanko koordinates: ({self.x},{self.y})")
        print(f"Atlikti suviai: {self.suviai}")
        print(f"Turimi taskai: {self.taskai}, numusti taikiniai: {self.score}")
        print(f"Taikinio koordinates: {self.taik}")

    def taikinys(self):
        self.taik = (random.randint(-10, 10), random.randint(-10, 10))

    def ar_pataike(self):
        if self.x == self.taik[0] and self.y == self.taik[1]:
            return ("Uzvaziuota ant taikinio!!")
        elif self.x == self.taik[0]:
            if self.y < self.taik[1] and self.kryptis == "Siaure":
                return ("Pataikyta!")
            elif self.y > self.taik[1] and self.kryptis == "Pietus":
                return ("Pataikyta!")
            else:
                return ("Nepataikyta")
        elif self.y == self.taik[1]:
            if self.x < self.taik[0] and self.kryptis == "Rytai":
                return ("Pataikyta!")
            elif self.x > self.taik[0] and self.kryptis == "Vakarai":
                return ("Pataikyta!")
            else:
                return ("Nepataikyta")
        else:
            return ("Nepataikyta")
