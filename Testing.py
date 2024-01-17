class animal:
    def __init__(self, name, height):
        self.__name = name
        self.height = height
    def makesound(self):
        print("Making sound")
    
    def getname(self):

        return self.__name
    
    def setname(self,newname):
        self.__name = newname

class Dog(animal):
    def __init__(self, name, height, breed):
        super().__init__(name,height)
        self.breed = breed
    def makesound(self):
        print("Woof")

def mthd1(animal):
    animal.makesound()
    print(animal.getname())
    animal.setname("New name")
    print(animal.getname())

animal1 = animal("dog", 20)
# print(animal1.getname())
# print(animal1.height)
# animal1.setname("horse")
# print(animal1.getname())
# print(animal1.makesound())

# animal2 = animal("cat", 10)
# print(animal2.name)
# print(animal2.height)

dog1 = Dog("niki", 15, "Lab")
# print(dog1.breed)
# dog1.makesound()


mthd1(animal1)
mthd1(dog1)