import random
print("Welcome to my game😊")

request = input("Do you want to play? ").lower()
if request=="yes":
    items = ["rock" , "paper", "scissors"]

    generated = random.choice(items)

    trials=0

    while True:
        trials+=1
        guess= input("Enter a guess: ")
        if guess not in items:
            print("Please enter the right word")
            continue
        elif guess ==generated:
            print(f"Correct guess")
            break
        else:
            print(f"The correct answer is {generated}")
            break
            
else:
    quit()