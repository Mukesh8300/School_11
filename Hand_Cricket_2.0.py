#HAND CRICKET
import random
print('''Welcome!
Lets Play HAND CRICKET
Rules:
1)Follow the instructions given properly
2)Runs are only allowed ranging1-6
3)Make sure u enjoy the game!''')
print()
#TOSS
print("Time for Toss")
x=1
while x==1:
    o_e=input("Odd or Even(o or e):")    
    if o_e!="o" and o_e!="e":
        print('''Invalid Choice
Try Again''')
    else:
        x=0
a=random.randint(1,6)
y=1
while y==1:
    try:
        b=int(input("Enter your choice(1-6):"))    
        if b>6 or b<0:
            print('''Invalid Choice
Try Again''')
        else:
            y=0
    except:
        print('''Invalid Choice
Try Again''')
print("Computer's choice:",a)
c=a+b
if o_e=="o":
    if c%2!=0:
        print("Your Won Toss")
        d=1
    else:
        print("Computer Won Toss")
        d=0
else:
    if c%2==0:
        print("Your Won Toss")
        d=1
    else:
        print("Computer Won Toss")
        d=0
if d==1:
    x=1
    while x==1:
        e=input("Bat or Bowl(ba or bo):")  
        if e!="ba" and e!="bo":
            print('''Invalid Choice
Try Again''')
        else:
            x=0
else:
    l=["Bat","Bowl"]
    e=random.randint(1,2)
    print("Computer's Choice:",l[e-1])
print()
#FIRST INNINGS
print("First innings")
target=0
if e=="ba" or e==2:
    x=1
    while x==1:
        ball1=random.randint(1,6)
        y=1
        while y==1:
            try:
                run1=int(input("Your Run(1-6):"))    
                if run1>6 or run1<0:
                    print('''Invalid Choice
Try Again''')
                else:
                    print("Comp Ball:",ball1)
                    y=0
            except:
                print('''Invalid Choice
Try Again''')
        if ball1==run1:
            x=0
            print("Wicket!")
            if target==0:
                print("Duck Out!!")
            print("You took",target,"runs")
            print("Computer needs",target+1,"runs to Win")
        else:
            target+=run1
else:
    x=1
    while x==1:
        run1=random.randint(1,6)
        y=1
        while y==1:
            try:
                ball1=int(input("Your Ball(1-6):"))    
                if ball1>6 or ball1<0:
                    print('''Invalid Choice
Try Again''')
                else:
                    print("Comp Run:",run1)
                    y=0
            except:
                print('''Invalid Choice
Try Again''')
        if ball1==run1:
            x=0
            print("Wicket!")
            if target==0:
                print("Duck Out!!")
            print("Computer took", target, "runs")
            print("You need",target+1,"runs to Win")
        else:
            target+=run1
print()
#SECOND INNINGS
print("Second innings")
chase=0
c2=0
if e=="bo" or e==1:
    x=1
    while x==1:
        ball2=random.randint(1,6)
        y=1
        while y==1:
            try:
                run2=int(input("Your Run(1-6):"))    
                if run2>6 or run2<0:
                    print('''Invalid Choice
Try Again''')
                else:
                    print("Comp Ball:",ball2)
                    chase+=run2
                    y=0
            except:
                print('''Invalid Choice
Try Again''') 
        if ball2==run2:
            print("Wicket!")
            if c2==0:
                print("Duck Out!!")
            x=0
            #SUPER OVER
            if target==c2:
                print("To Win",target+1,"runs")
                print("You Chased",c2,"runs")
                print("Draw!")
                print()
                print("Super Over!")
                x=1
                while x==1:
                    print('''Rules:
1)There are totally 6 balls (ie) 1 over
2)The person who was batting at the first innings will bat now
3)If out, that run is not added other runs are added ''')
                    print()
                    print("First innings")
                    runs1=0
                    for i in range(6):
                        srun1=random.randint(1,6)
                        y=1
                        while y==1:
                            try:
                                sball1=int(input("Your Ball(1-6):"))    
                                if sball1>6 or sball1<0:
                                    print('''Invalid Choice
Try Again''')
                                else:
                                    print("Comp Run:",srun1)
                                    y=0
                            except:
                                print('''Invalid Choice
Try Again''')
                        if srun1!=sball1:
                            runs1+=srun1
                    print("Computer took",runs1,"runs")
                    print("You need",runs1+1,"runs to Win")
                    print()
                    runs2=0
                    for j in range(6):
                        if runs2>runs1:
                            break
                        print("Second innings")
                        sball2=random.randint(1,6)
                        y=1
                        while y==1:
                            try:
                                srun2=int(input("Your Run(1-6):"))    
                                if srun2>6 or srun2<0:
                                    print('''Invalid Choice
Try Again''')
                                else:
                                    print("Comp Ball:",sball2)
                                    y=0
                            except:
                                print('''Invalid Choice
Try Again''')
                        if srun2!=sball2:     
                            runs2+=srun2
                    if runs1==runs2:
                        print("To Win",runs1+1,"runs")
                        print("You Chased",runs2,"runs")
                        print("Draw!")
                        print()
                        print("Super Over again!")
                    else:
                        x=0
                        print("To Win",runs1+1,"runs")
                        print("You Chased",runs2,"runs")
                        if runs2>runs1:
                            print("YOU WON!")
                        else:
                            print("YOU LOSE!")
            else:
                print()
                print("To Win",target+1,"runs")
                print("You Chased",c2,"runs")
                print("YOU LOST!")
        elif chase>target:
            print()
            print("To Win",target+1,"runs")
            print("You Chased",chase,"runs")
            print("YOU WIN!")
            x=0
        else:
            c2+=run2
else:
    x=1
    while x==1:
        run2=random.randint(1,6)
        y=1
        while y==1:
            try:
                ball2=int(input("Your Ball(1-6):"))    
                if ball2>6 or ball2<0:
                    print('''Invalid Choice
Try Again''')
                else:
                    print("Comp Run:",run2)
                    chase+=run2
                    y=0
            except:
                print('''Invalid Choice
Try Again''')
        if ball2==run2:
            print("Wicket!")
            if c2==0:
                print("Duck Out!!")
            x=0
            #SUPER OVER
            if target==c2:
                print("To Win",target+1,"runs")
                print("Computer Chased",c2,"runs")
                print("Draw!")
                print()
                print("Super Over!")
                x=1
                while x==1:
                    print('''Rules:
1)There are totally 6 balls (ie) 1 over
2)The person who was batting at the first innings will bat now
3)If out, that run is not added other runs are added ''')
                    print()
                    print("First innings")
                    runs1=0
                    for i in range(6):
                        sball1=random.randint(1,6)
                        y=1
                        while y==1:
                            try:
                                srun1=int(input("Your Run(1-6):"))    
                                if srun1>6 or srun1<0:
                                    print('''Invalid Choice
Try Again''')
                                else:
                                    print("Comp Ball:",sball1)
                                    y=0
                            except:
                                print('''Invalid Choice
Try Again''')
                        if srun1!=sball1:
                            runs1+=srun1
                    print("You took",runs1,"runs")
                    print("Computer needs",runs1+1,"runs to Win")
                    print()
                    print("Second innings")
                    runs2=0
                    for j in range(6):
                        if runs2>runs1:
                            break
                        srun2=random.randint(1,6)
                        y=1
                        while y==1:
                            try:
                                sball2=int(input("Your Ball(1-6):"))    
                                if sball2>6 or sball2<0:
                                    print('''Invalid Choice
Try Again''')
                                else:
                                    print("Comp Run:",srun2)
                                    y=0
                            except:
                                print('''Invalid Choice
Try Again''')
                        if srun2!=sball2:     
                            run2+=srun2
                    if runs1==runs2:
                        print("To Win",runs1+1,"runs")
                        print("Computer Chased",runs2,"runs")
                        print("Draw!")
                        print()
                        print("Super Over again!")
                    else:
                        x=0
                        print("To Win",runs1+1,"runs")
                        print("Computer Chased",runs2,"runs")
                        if runs2<runs1:
                            print("YOU WON!")
                        else:
                            print("YOU LOSE!")
            else:
                print()
                print("To Win",target+1,"runs")
                print("Computer Chased",c2,"runs")
                print("YOU WON!")
        elif chase>target:
            print()
            print("To Win",target+1,"runs")
            print("Computer Chased",chase,"runs")
            print("YOU LOST!")
            x=0
        else:
            c2+=run2
