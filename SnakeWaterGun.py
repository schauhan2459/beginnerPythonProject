#Snake Water Gun

import random

def game():
    n=int(input("\nEnter no. of round you want to play: "))
    p=0
    c=0
    t=0

    while n>t:
        choice=["Snake","Water","Gun"]
        print("\n----------------------------------\n")
        print(F"Available roles are:")
        print(f"1. {choice[0]}  2. {choice[1]}  3. {choice[2]}")
        r=str(input("Enter your choice: "))
        cp=random.choice(choice)
        print(f"Computer Choice: {cp}")
        
        if r==cp:
            print("Draw")
            c=c+1
            p=p+1
            print(f"you:{p} computer:{c}\n")
        elif r=="Snake" and cp=="Water":
            print("You won")
            c=c
            p=p+1
            print(f"you:{p} computer:{c}\n")
        elif r=="Snake" and cp=="Gun":
            print("You lose")
            c=c+1
            p=p
            print(f"you:{p} computer:{c}\n")
        elif r=="Water" and cp=="Snake":
            print("You lose")
            c=c+1
            p=p
            print(f"you:{p} computer:{c}\n")
        elif r=="Water" and cp=="Gun":
            print("You Won")
            c=c
            p=p+1
            print(f"you:{p} computer:{c}\n")
        elif r=="Gun" and cp=="Snake":
            print("\nYou Won")
            c=c
            p=p+1
            print(f"you:{p} computer:{c}\n")
        elif r=="Gun" and cp=="Water":
            print("You lose")
            c=c+1
            p=p
            print(f"you:{p} computer:{c}\n")
        else:
            print("Invalid Choice.Try Again!")
            break
        t=t+1
    
    print("----------------------------------\n")
    if p<c:
        print("Final : Computer Win!!")
        print(f"You:{p} Computer:{c}")
    elif p==c:
        print("Final : Draw")
        print(f"You:{p} Computer:{c}")
    else:
        print("Final : You Win!!")
        print(f"You:{p} Computer:{c}")
    print("\n----------------------------------")
        
game()