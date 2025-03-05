import random
print("Rock Paper Scissors")
print("Best of 5, Wins!")
print('''1-Rock
2-Paper
3-scissors''')
l=["Rock","Paper","Scissors"]
i=0
lc=0
wc=0
while i<5:
    if lc==3 or wc==3:
        break
    else:
        a=random.randint(1,3)
        b=int(input("Enter your choice(1-3):"))
        print("You:",l[b-1])
        print("Computer:",l[a-1])
        if a==1:
            if b==1:
                print("Draw")
            elif b==2:
                print("You win")
                wc+=1
                i+=1
            else:
                print("You lose")
                lc+=1
                i+=1
        elif a==2:
            if b==2:
                print("Draw")
            elif b==3:
                print("You win")
                wc+=1
                i+=1
            else:
                print("You lose")
                lc+=1
                i+=1
        else:
            if b==3:
                print("Draw")
            elif b==1:
                print("You win")
                wc+=1
                i+=1
            else:
                print("You lose")
                lc+=1
                i+=1
print("Best of 5, Wins!")
if wc>lc:
    print("YOU WIN! :)")
else:
    print("YOU LOSE! :(")
print("You:",wc)
print("computer",lc)
