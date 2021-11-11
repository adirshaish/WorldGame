import random


def GuessGame(num2):
    options = input("Continue from last run [Y]es/[N]o ?")
    if options == "Y":
        fd = open("save.db", "r")
        data = fd.read()
        data = data.split("|")
        rand = int(data[0])
        tries = int(data[1])
        fd.close()
    else:
        rand = random.randint(1, num2 + 1)
        tries = 0

    while True:
        user_guess = input("What is the number [S]ave? > ")
        if user_guess == "S":
            fd = open("save.db", "w")
            fd.write("{0}|{1}".format(rand, tries))
            fd.close()
            exit(0)
        try:
            user_guess = int(user_guess)
        except:
            while not user_guess.isdigit():
                user_guess = input("No entry number Enter number please:")
                user_guess = int(user_guess)
        if user_guess == rand:
            break
        elif user_guess > rand:
            print("Your number is bigger")
            tries += 1
        else:
            print("Your number is lower")
            tries += 1

    print("You win in {0} tries".format(tries))
