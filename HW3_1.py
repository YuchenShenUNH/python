def bunnyEars(bunnies):
    if(bunnies==0):
        return 0
    elif (bunnies%2 ==1):
        return 3+ bunnyEars(bunnies-1)
    else:
        return 2+ bunnyEars(bunnies-1)

print(bunnyEars(0))
print(bunnyEars(1))
print(bunnyEars(2))
print(bunnyEars(3))
print(bunnyEars(4))
