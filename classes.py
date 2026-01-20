# class 

greet = "Good Morning"

class PersonDetails():
    
    # # global name2
    # name2 = "Sandeep"
    
    def __init__(self, name):
        self.name = name
        self.__name2 = "Sandeep"
        # print("Hey, this is constructer method")
        
    def greet(self):
        return f"Hey {self.name}, {greet}", self.__message()
    
    def __message(self):  # private method
        return "How are you doing?"


person1 = PersonDetails("Dileep")
# print(person1.greet())
print(person1.__name2)
# print(person1.__message())

# person2 = PersonDetails("Geetha")
# print(person2.greet())

# global
# local
# non locals