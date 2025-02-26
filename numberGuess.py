#comp asks for a random number
# user inputs 
#comp generates a random number
# the comp tells the user whether the number inputed is similar to the generated number
import random

generated = random.randint(0, 10)

trials = 0
while True:
    trials += 1
    number = input("Enter a guess: ")
    if number.isdigit():
        number = int(number)
    else:
        print("Type a number")
        continue

    if number==generated:
        print("The answer is correct")
        break
    elif number>generated:
            print("Too large")
    else:
        print("Too small")

print(f"Congraturations You got it in {trials} guesses")

