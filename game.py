import random
import random as r


rnum=random.randint(1,1000)

while True:
    print("Print 1 to stop this game")
    num = int(input("Enter number between 1 to 1000="))
    if(num==1):
        break
    elif num>rnum:
        print("Your prediction is so high")
    elif num==rnum:
        print("Your Win this game")
        break
    else:
        print("Your prediction is so low")


