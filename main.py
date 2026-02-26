import random
game = random.randint(1, 100)
print("Guess the number I'm thinking of (1 to 100)")
#q = quit of game
#print(game) = cheatcode
popytki = 0
while True:
    chislo = input("Your number:").strip()

    if chislo == "q":
        print("Bye,number was:", game)
        break

    if not chislo.isdigit():
        print("Only numbers btw...")
        continue


    otvet = int(chislo)

    if otvet > 100:
        print("Only up to 100 bro...")
        continue

    if otvet < 1:
        print("Cannot be lower than 1 bro...")
        continue


    popytki += 1

    if otvet == game:
        print("Nice!Were attempts:", popytki)
        break

    elif otvet<game:
        print("Too low")

    elif otvet>game:
        print("Too much")

