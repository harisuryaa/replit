#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

rand_num = random.randint(1, 100)

number = int(input("guess a number between 1 and 100: "))
guess = False

def compare(rand_num, number):
    if number > rand_num:
        print("Too high")
        global guess 
        guess = False


    elif number < rand_num:
        print("Too low")
        global guess 
        guess = False
        
    elif number==rand_num:
        print(f"You got it the answer is {rand_num}")
        global guess 
        guess = True

