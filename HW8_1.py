class Animal:
    def __init__(self, name):
        self.name = name
        if name=="elephant":
            self.info=['I am the largest land-living mammal in the world','I am haviest animal can walk','I am kind so I like people']
        if name== "tiger":
            self.info=['I am the biggest cat','I am the prince of land','I am eating meat only']
        if name== "bat":
            self.info=['I use echo-location','I can fly','I see well in dark']
    def guess_who_am_i(self):
        hints=0
        print("I will give you 3 hint, guess what animal I am")
        print("I have exceptional memory")
        Q=input("who am I?")
        if Q == self.name:
            print("You are right! I am",self.name)
        while(Q!=self.name and hints!=3):
            print(self.info[hints])
            hints=hints+1
            Q=input("who am I?")
            if Q!= self.name and hints<3:
                print("Nope,try again!")
            elif Q!=self.name and hints==3:
                print("I am out of hints! My name is ",self.name)
                break
            elif Q==self.name:
                print("You got is! I am",self.name)
                break



e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
