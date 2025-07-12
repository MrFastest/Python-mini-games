import random as rd

start_range=input("Enter the start range for making a guess :")
if start_range.isdigit():
    start_range=int(start_range)
    
    if start_range<=0:
        print("Enter number larger than 0")
        quit()

else:
    quit()
    
r = rd.randrange(0,start_range+1)
count = 1
while True:
    no = input("Enter the value to guess:")
    if no.isdigit():
        no=int(no)
    
    if no<=0:
        print("Enter number larger than 0")
        continue
    
    if no == r:
        print("You Got it..!!")
        print("You guessed answer correctly in",count,"chances")
        break
    else:
        count+=1
        print("Ooops!!. You got it wrong..")
        #2print(r)
    