import sys
import random
from enum import Enum
class RPS(Enum):
    ROCK = 1
    SCISSOR = 2
    PAPER= 3
playagain=True
while playagain:
    user=int(input("Enter choice\n1:Rock\n2:scissor\n3:paper\n\n"))
    if user<1 or user>3:
        sys.exit("enter from 1 to 3")
    computer=random.choice("123")
    computerchoice=int(computer)
    print("user choice:"+str(RPS(user)).replace("RPS."," ")+".")
    print("computer choice:"+str(RPS(computerchoice)).replace("RPS."," ")+".")
    if user==1 and computerchoice==2:
        print("😍you win")
    elif user==2 and computerchoice==3:
        print("👌 you win")
    elif user==3 and computerchoice==1:
        print("😘you win")
    elif user==computerchoice:
        print("😁Tie")
    else:
        print("💕Computer WINS")
    Again = input("Enter Y for Yes and Q for quit\n")
    if Again.lower()=="y":
        continue
    else:
        playagain=False
        print("Thank You")