low = 0
height =100
mid =50
turn=1




name=input("What is your name?")
print("Hello "+name+" ! Let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")
flag=input("Is it "+ str(mid) + "?(yes/no)")
while (flag=="no"):
	turn=turn+1
	compare= input("Is the number larger than "+str(mid) +"?(yes/no)")
	if(compare=="yes"):
		low=mid
		mid=(low+height)//2
		flag=input("Is it "+ str(mid) + "?(yes/no)")
	if (compare=="no"):
		height=mid
		mid=(low+height)//2
		flag=input("Is it "+ str(mid) + "?(yes/no)")
while (flag=="yes"):
	print("Yeey! I got it in "+str(turn)+" tries!")
	break
		
	
