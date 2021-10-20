#################################################
# example of factory pattern:

# class Person: 
#     def __init__(self): 
#         self.name = None 
#         self.gender = None 
  
#     def getName(self): 
#         return self.name 

#     def getGender(self): 
#         return self.gender 


# class Male(Person): 
#     def __init__(self, name): 
#         print("Hello Mr. " + name) 

# class Female(Person): 
#     def __init__(self, name): 
#         print ("Hello Miss. " + name) 

# class Factory: 

  
#     def getPerson(self, name, gender): 
#         if gender == 'M': 
#             return Male(name) 
#         if gender == 'F': 
#             return Female(name) 

# f = Factory()

# print(f.getPerson('connor', 'F'))



#################################################
# example of proxy pattern - athlete (Real Subject) and coach (Proxy)
from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.majors = True
        self.injured = False
        self.pay = randint(1200000, 6000000)
        self.injury = ''

    def recovered(self):
        self.injured = False

class Coach:
    def __init__(self, name):
        self.name = name

    def gotHurt(self, player, injury):
        player.injured = True
        self.player = player
        self.injury = injury 

    def sendtoAAA(self, player):
        if player.injured == True:
            player.majors = False
            print(f'sending {player.name} down to AAA to recover from a {self.injury} injury')
        else:
            print(f'{player.name} is good and healthy. Let\'s keep him up here.')


if __name__ == '__main__':
    
    rizz = Player('Anthony Rizzo')
    boone = Coach('Aaron Boone')

    print(rizz.majors)
    boone.gotHurt(rizz, 'hamstring')
    boone.sendtoAAA(rizz)
    print(rizz.majors)

    