import math
import random

def calculate_die_number(points, n):
    die_number_n_value = (math.floor(points // (6 ** n)) % 6) + 1
    return die_number_n_value

# Example usage
dice_line = 2
points = 36
n = 3
total_dice= (dice_line**3)

while True:
    input("Press enter to roll the d6: ")
    roll_result = random.randint(1, 6)
    points += roll_result
    result = calculate_die_number(points, n)
    print(f"Rolled: {roll_result}")
    print(f"Die number for {points} points and n-dice = {n} is: {result}")

    if points >= 41:
        print("Test")
        print(total_dice)
