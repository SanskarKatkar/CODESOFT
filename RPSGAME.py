import sys
import random
from enum import Enum
def playrps():
    count=0
    playerwin=0
    computerwin=0
    def rps():
        nonlocal playerwin
        nonlocal computerwin
        class RPS(Enum):
            ROCK = 1
            SCISSOR = 2
            PAPER = 3
        user=int(input("Enter choice\n1:Rock\n2:scissor\n3:paper\n\n"))
        if user not in[1,2,3]:
            print("Enter from 1 to 3")
            return rps()
        if user<1 or user>3:
            sys.exit("enter from 1 to 3")
        computer=random.choice("123")
        computerchoice=int(computer)
        print(f"user choice:{str(RPS(user)).replace('RPS.',' ').title()}")
        print(f"computer choice: {str(RPS(computerchoice)).replace('RPS.',' ').title()}")
        def decide(user,computerchoice):
            nonlocal playerwin
            nonlocal computerwin
            if user==1 and computerchoice==2:
                playerwin+=1
                return "😍you win"
            elif user==2 and computerchoice==3:
                playerwin+=1
                return "👌 you win"
            elif user==3 and computerchoice==1:
                playerwin+=1
                return "😘you win"
            elif user==computerchoice:
                return "😁Tie"
            else:
                computerwin+=1
                return "💕Computer WINS"
        result=decide(user,computerchoice)
        print(result)
        nonlocal count
        count+=1
        print(f"COUNT: {count}")
        print(f"PlayerwinCOUNT: {playerwin}")
        print(f"computerwinCOUNT: {computerwin}")
        print("play again?")
        while True:
            Again = input("Enter Y for Yes and Q for quit\n")
            if Again.lower() not in ["y","q"]:
                continue
            else:
                break
        if Again.lower()=="y":
            rps()
        else:
            print("Thank You")
            sys.exit("GAME OVER")
    return rps
play=playrps()
play()