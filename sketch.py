class Person: 
    def __init__(self): 
        self.name = None 
        self.gender = None 
  
    def getName(self): 
        return self.name 

    def getGender(self): 
        return self.gender 


class Male(Person): 
    def __init__(self, name): 
        print("Hello Mr. " + name) 

class Female(Person): 
    def __init__(self, name): 
        print ("Hello Miss. " + name) 

class Factory: 

  
    def getPerson(self, name, gender): 
        if gender == 'M': 
            return Male(name) 
        if gender == 'F': 
            return Female(name) 

f = Factory()



print(f.getPerson('connor', 'F'))