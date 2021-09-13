import random
import sys


def result(op1, op2):
    if op1 == op2:
        print("There is a draw ({})".format(op1))
        return 50
    else:
        index1 = options.index(op1)
        index2 = options.index(op2)
        half = len(options) // 2
        if index2 > index1 and index2 - index1 <= half or \
                index2 < index1 and index1 - index2 > half:
            print(f"Well done. The computer chose {op1} and failed")
            return 100
        else:
            print(f"Sorry, but the computer chose {op1}")
            return 0


name = input("Enter your name: ")
print(f"Hello, {name}")
file = open("rating.txt", "r", encoding="utf-8")
lines = file.readlines()
lines = [line.rstrip() for line in lines]
lines = [line.split() for line in lines]
scores = {player: int(score) for player, score in lines}
file.close()

options = input()
if options:
    options = options.split(",")
    options = [option.strip().lower() for option in options]
else:
    options = ["scissors", "rock", "paper"]

print("Okay, let's start")
while True:
    user = input()
    if user == "!exit":
        print("Bye!")
        sys.exit()
    elif user == "!rating":
        print(f"Your rating: {scores[name]}")
    elif user not in options:
        print("Invalid input")
    else:
        points = result(random.choice(options), user)
        score = scores.setdefault(name, 0)
        scores.update({name: score + points})
