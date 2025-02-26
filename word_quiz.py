#The comp asks a question 
#user types an answer
#comp checks whether it is the correct answer and it marks it as correct or incorrect
#comp calculates the total correct answers and the percentage
score = 0
count = 0
answer = input("What does RAM stand for? ").lower()
count+=1
if answer == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ").lower()
count+=1
if answer == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ").lower()
count+=1
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
count+=1
if answer == "graphic processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"You've got {score} out of {count}, {(score/count)*100}%")

