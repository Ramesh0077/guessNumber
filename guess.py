import random
randnumber=random.randint(1,101)
print(randnumber)
userguess=None
guess=0
while(userguess!=randnumber):
    userguess=int(input("Enter the number--"))
    if userguess>randnumber:
        print("Enter lesser number!")
    elif userguess<randnumber:
        print("ENter higher number!")
    else:
        print("you guess it right!")
    guess=guess+1
    exit
print("you took ",guess, "round to win the game!")
with open("highscore.txt",'r') as f:
    high_score=int(f.read())
if(guess<high_score):
    print("congratulation you have broken the high score!")
    with open("highscore.txt","w") as f:
        f.write(str(guess))