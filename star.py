import os

# os.system('cls')
input=7



if input%2==0:
    for i in range(1,int(input/2)+1):
        for _ in range(i):
            print("*",end="")
        print() 

    for i in range(int(input/2),0,-1):
        for _ in range(i):
            print("*",end="")
        print()           
    
else:
    for i in range(1,int(input/2)+1):
        for _ in range(i):
            print("*",end="")
        print() 
    for i in range(int(input/2)+1,0,-1):
        for _ in range(i):
            print("*",end="")
        print()   
