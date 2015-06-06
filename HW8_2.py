from random import randrange

print("INTEGER DIVISIONS")

while True:
        a = randrange(8) 
        b = randrange(25)        
        
        try:
            if b%a==0:
                Q=int(input('%d / %s ='%(b,a)))
                if int(Q) == (b//a):
                    print("CORRECT!")
                else:
                    print("INCORRECT!")
        except ValueError:
                print("Please enter Integers Only!")
        except ZeroDivisionError:
            a = randrange(8)
