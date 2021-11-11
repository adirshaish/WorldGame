import random
from time import sleep


def generate_sequence(num2):
    rand = []
    for i in range(num2):
        rand.append(random.randint(1, 101))
    print_rend(rand)
    get_list_from_user(rand, num2)


def print_rend(rand):
    print("\r", rand, end="")
    sleep(0.7)
    print("\rTime's running out It's time to guess")


def get_list_from_user(rand, num2):
    user_number = []
    for i in range(num2):
        user_number.append(int(input("Hi enter the numbers you saw:>")))
    if rand == user_number:
        num3 = 1
        fd = open("save1.db", "w")
        fd.write("{0}".format(num3))
        fd.close()
    else:
        num3 = 0
        fd = open("save1.db", "w")
        fd.write("{0}".format(num3))
        fd.close()


def play(num2):
    generate_sequence(num2)
    fd = open("save1.db", "r")
    data = fd.read()
    num3 = int(data[0])
    fd.close()
    if num3 == 1:
        print("You Win!!")
    else:
        print("Not this time will you try again")
