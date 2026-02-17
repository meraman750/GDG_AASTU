def add(a,b):
    print( a + b)
def subtract(a,b):
    print( a - b)
def multiplay(a,b):
     print(a * b)
def divide(a,b):
    if b==0:
        print("Invlaid")
    else:    
        print(a/b)   

a=float(input("The first number: "))
b=float(input("The second number: "))      


while True:
    choose=int(input("To Add press 1\nTo perform subtraction press 2\nTo multiplay press 3\nTo Divide press 4\nTo Terminate press 5\n"))

    if choose==5:
      print("Exit")
      break
   
    elif choose==1:
        add(a,b)
    elif choose==2:
        subtract(a,b)
    elif choose==3:
        multiplay(a,b)
    elif choose==4:
        divide(a,b)
    else:
        print("Invalid input")    
    
       
