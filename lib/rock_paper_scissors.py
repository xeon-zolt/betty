import random

values = {
        1 : "rock",
        2 : "paper",
        3 : "scissors"
    }


def judge(user,comp):
    if(user == 1):
        if(comp == 2):
            print("Computer wins")
        elif(comp == 1):
            print("Draw")
        else:
            print("Human Wins")

    elif(user == 2):
        if(comp == 3):
            print("Computer wins")
        elif(comp == 2):
            print("Draw")
        else:
            print("Human Wins")

    else:
        if(comp == 1):
            print("Computer wins")
        elif(comp == 3):
            print("Draw")
        else:
            print("Human Wins")
            
def play(user):
    comp = random.randint(1,3)
    print("Human = %s"%values[user])
    print("Computer = %s"%values[comp])
    judge(user,comp)



        
