

def count_frequency(mylist):
    count_frequency={}
    for item in mylist:
        if item in count_frequency.keys():
            count_frequency[item]+=1
        else:
            count_frequency[item]=1
    return count_frequency

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
    
print (count_frequency(mylist))
