from tankas import Tankas, pickle

while True:
    choice1 = input("z - naujas zaidimas\nt - rezultatai\nv - isvalyti rezultatus\ni - iseiti\n")
    match choice1:
        case "z":
            tankas = Tankas()
            while True:
                choice2 = input(
                    "w - pirmyn \na - kairen\ns - atgal\nd - desinen\nx - sauti\ni - iseiti i main menu :)\n")
                match choice2:
                    case "w":
                        tankas.pirmyn()
                    case "a":
                        tankas.kairen()
                    case "s":
                        tankas.atgal()
                    case "d":
                        tankas.desinen()
                    case "x":
                        tankas.suvis()
                    case "i":
                        break
                    case _:
                        print("Neteisingai pasirinktas veiksmas")
        case "t":
            try:
                with open("rezultatai.pkl", "rb") as file:
                    highscores = pickle.load(file)
                    for x in highscores:
                        print(x)
            except:
                print("Sarasas tuscias")

        case "v":
            with open("rezultatai.pkl", "wb") as file:
                a = []
                pickle.dump(a, file)
        case "i":
            break
        case _:
            print("Neteisingai pasirinktas veiksmas")
