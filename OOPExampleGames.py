import time, sys, random

def faulty_input():
    print("!Missing or Faulty Input")

def add_point():
    print(".")
    time.sleep(.3)
    print(". .")
    time.sleep(.3)
    print(". . .")
    time.sleep(.3)

class Player():
    def __init__(self, name, health = 10, power = 100, score = 10):
        self.name = name
        self.health = health
        self.power = power
        self.score = score

    def show_info(self):
        print("""
        Name: {}
        Health: {}
        Power: {}
        Score: {}
        """.format(self.name, self.health, self.power, self.score))

    def attack(self, enemy):
        result = self.attack_defend_count()
        if(result == 1):
            print("The Attack has Begun...")
            add_point()
            print("Attack is Successful")
            self.power -= 8
            self.score += 10
            enemy.health -= 1
            self.show_info()
            enemy.show_info()
        else:
            print("The Attack has Begun...")
            add_point()
            print("Attack is Unsuccessful")
            self.power -= 8
            self.health -= 1
            enemy.score += 10
            self.show_info()
            enemy.show_info()

    def defend(self, enemy):
        result = self.attack_defend_count()
        if (result == 1):
            print("The Defence has Begun...")
            add_point()
            print("defend is Successful")
            enemy.power -= 8
            self.score += 10
            enemy.health -= 1
            self.show_info()
            enemy.show_info()
        else:
            print("The Defence has Begun...")
            add_point()
            print("Defend is Unsuccessful")
            self.power -= 8
            self.health -= 1
            enemy.score += 10
            self.show_info()
            enemy.show_info()

    def attack_defend_count(self):
        return random.randint(1,2)

    def exit(self):
        print("Game is Closing...")
        add_point()
        sys.exit()

player1 = Player(input("Please Write Your Player-1 Name: "))
player2 = Player(input("Please Write Your Player-2 Name: "))

print("Game is Starting...")
add_point()

while True:
    options = input("""
    1-Attack
    2-Defence
    3-Exit
    Option: 
    """)

    if(options == "1"):
        player1.attack(player2)
    elif(options == "2"):
        player1.defend(player2)
    elif(options == "3"):
        player1.exit()
    else:
        faulty_input()

    if(player1.score == 100 or player2.health == 0 or player2.power <= 0):
        print("Winner of The Game is:",player1.name)
        break
    if(player2.score == 100 or player1.health == 0 or player1.power <= 0):
        print("Winner of The Game is:", player2.name)
        break
