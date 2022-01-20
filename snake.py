import random
def game(computer,you):
    if computer==you:
        return None
    elif computer=='s':
        if you=='g':
            return TRUE
        elif you=='w':
            return False
    elif computer=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif computer=='g':
        if you=='w':
            return True
        elif you=='s':
            return False

print("computer turn: snake(s) water(w) gun(g):")
randno=random.randint(1,3)
if randno==1:
    computer='s'
elif randno==2:
    computer='w'
elif randno==3:
    computer='g'
you=input("Your turn: snake(s) water(w) gun(g): ")
a=game(computer,you)
print(f'computer choose {computer}')
print(f"you choose {you}")

if a== None:
    print("game is tie!")
elif a==True:
    print("you win!")
else:
    print("computer win!")