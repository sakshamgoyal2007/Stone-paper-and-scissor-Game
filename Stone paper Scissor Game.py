import random
print("Hi Guys😃😃")
''' 1 for stone
2 for paper
3 for scissor '''

print("YOU ARE PLAYING STONE-PAPER-SCISSOR WITH CONPUTER")
C=random.choice([1,2,3])
choicedict={1:"s",2:"p",3:"c"}
reversedict={"s":1,"p":2,"c":3}
print("s for stone\np for paper\nc for scissor")

def game():
    youstr=input("Enter your choice : ")
    you=reversedict[youstr]
    print("Computer Choice:",choicedict[C],"\nYours Choice:",choicedict[you])
    if(C==you):
        print("Draw😐")
    else:
        if(C==1 and you==2):
            print("You Win😃")
            
        elif(C==1 and you==3):
            print("You lose😭")
           
        elif(C==2 and you==1):
            print("You lose😭")
            
        elif(C==2 and you==3):
            print("You Win😃")
            
        elif(C==3 and you==1):
            print("You Win😃")
            
        elif(C==3 and you==2):
            print("You lose😭")
            
        else:
            print("Something Went Wrong🤔")
            
               
R=input("You Are Ready To Play This Game : ")
if R=="y":
    game()
else:
    print("Thank You")
    
