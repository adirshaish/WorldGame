from GuessGame import GuessGame
from MemoryGame import play
from CurrencyRouletteGame import play3


def welcome(name):
    print("Hello {0} and welcome to the World of Games (WoG)"
          "Here you can find many cool games to play.".format(name))


def load_game():
    num = input("Please choose a game to play: \n"
                "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n "
                "2.Guess Game - guess a number and see if you chose like the computer \n  "
                "3. Currency Roulette - try and guess the value of a random amount of USD in ILS: > ")
    num2 = input("Please choose game difficulty from 1 to 5: > ")
    Checking_number(num, num2)
    Check_if_number_in_range(num, num2)
    if num == "1":
        GuessGame(int(num2))
    elif num == "2":
        play(int(num2))
    elif num == "3":
        play3(int(num2))


def Checking_number(num, num2):
    while not num.isdigit():
        num = input("No entry number Enter number please")
    while not num2.isdigit():
        num2 = input("No entry number Enter number please")


def Check_if_number_in_range(num, num2):
    num = int(num)
    num2 = int(num2)
    if not 1 <= num <= 3:
        print("The first number is out of range {0}!!".format(num))
    if not 1 <= num2 <= 5:
        print("The second number is out of range {0}!!".format(num2))
