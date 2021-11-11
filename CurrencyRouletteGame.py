import random
import requests


def get_money_interval(num3, rand):
    response = requests.get(
        "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=e6a034bf73ace36767f4")
    rate = response.json()["USD_ILS"]
    min_guess = int(rand * rate - (5 - int(num3)))
    max_guess = int(rand * rate + (5 - int(num3)))
    return min_guess, max_guess


def get_guess_from_user(rand):
    guess = input("Enter your guess for {0} USD".format(rand))
    return guess


def play3(num2):
    rand = random.randint(1, 100)
    guess = get_guess_from_user(rand)
    min_guess, max_guess = get_money_interval(rand, num2)
    if min_guess <= int(guess) <= max_guess:
        print("you Win!!")
    else:
        print("Not this time will you try again")
