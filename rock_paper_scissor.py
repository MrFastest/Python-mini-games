import random

user_wins= 0
computer_wins=0

options = ["rock","paper","scissors"]

count = int(input("Enter how many rounds u have to play with computer..."))
i = 0
while (i!=count):
    user_input= input("Type rock/paper/scissors to Play or Q to quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    
    print("Computer picked "+computer_pick+".")
    
    if user_input=="rock" and computer_pick=="scissors":
        print("You Won")
        user_wins+=1
        
    elif user_input=="paper" and computer_pick=="rock":
        print("You Won")
        user_wins+=1
    
    elif user_input=="scissors" and computer_pick=="paper":
        print("You Won")
        user_wins+=1
        
    elif user_input==computer_pick:
        print("Draw ..")
    
    else:
        print("You Lostt..")
        computer_wins+=1
    i = i+1
    
        
print("You Won",user_wins,"times")
print("Computer wins",computer_wins,"times")
print("Good Bye KAS")