# Option 3 - Dice Game
import random


start = input("Welcome! Type START to begin the game!!!! ")
stop = False
user_points = 0
cpu_points = 0

while not stop:
    user_dice = random.randint(1,6)
    cpu = random.randint(1,6)

    if user_dice > cpu:
        print(f"YOU HAVE WON!\nYou rolled: {user_dice}\nCPU rolled: {cpu}")
        user_points += 10
    elif cpu > user_dice:
        print(f"YOU HAVE LOST \nYou rolled: {user_dice} \nCPU rolled: {cpu} ")
        cpu_points += 10
    else:
        print(f"DRAW\nYou rolled: {user_dice}\nCPU rolled: {cpu}")

    play_again = input("Would you like to continue? ")

    if play_again == "no":
        print(f"You have scored: {user_points} \n CPU has scored: {cpu_points}")
        stop = True
    else:
        print(f"You have scored: {user_points} \n CPU has scored: {cpu_points}")

    if user_points == 30:
        print("You have won")
        stop = True
    if cpu_points == 30:
        print("Game Over you have lost!")
        stop = True



