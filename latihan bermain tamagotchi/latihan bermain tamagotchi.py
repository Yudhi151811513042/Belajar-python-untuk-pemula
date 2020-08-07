name = input('Nama monsternya siapa ? ')
monster = {'name': name, 'power': 100}

def startGame():
    choice = input("Mau apa ? 1.Makan 2.LihatStatus 3.Keluar ")
    if choice == '1':
        goEat()
    elif choice == '2':
        goCheck()
    else:
        goExit()

def goEat():
    print("nyam .. nyam ..")
    monster['power'] += 100
    startGame()
def goCheck():
    print("check .. check ..")
    print(monster)
    startGame()
def goExit():
    print("bye .. bye ..")

startGame()

