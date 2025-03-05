'''
1 for snake
-1 is water 
0 is gun
'''
import random
computer=random.choice([-1,0,1])
youstr=input("enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")
# you=youDict[youstr]
if(computer== you):
    print("its draw")
else:
    
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you loss")
    elif(computer==1 and you==-1):
        print("you loss")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==11):
        print("you loss")
    else:
        print("something went wrong")

    

