# object oriented programming


# 1. Encapsulation
# 2. Inherietence 
# 3. Polymorphism
# 4. Abstraction

class BankAccount():
    def __init__(self, balance: int):
        self.__balance = balance  # private variable
        self.amount = 2000
    
    def get_balance(self):
        return self.__balance

# b = BankAccount(10_000)
# print(b.amount)
# print(b.get_balance())
# print(b.__balance)

# Inheritance

# --> single inhertance
# --> multiple inheritance
# --> multi-level inheritance
# --> hybrid inheritance

# parent class / base class
# child class / derived class


# parent class
class Animal:
    def eat(self):
        print("Eating")

# child class
class Dog(Animal):
    def bark(self):
        print("Barking")

tommy = Dog()
tommy.eat()
tommy.bark()


class GrandFather: # parent class
    def get_grand_fathers_properties(self):
        print("owns a property in Mumbai")


class Father: # parent class
    def get_fathers_properties(self):
        print("owns a complex in Bangalore")


class Son(GrandFather, Father):  # child class
    def get_son_properties(self):
        print("owns a bike")
        

# Harsha = Son()
# Harsha.get_fathers_properties()
# Harsha.get_grand_fathers_properties()
# Harsha.get_son_properties()


class GrandFather: # parent class
    def get_grand_fathers_properties(self):
        print("owns a property in Mumbai")


class Father(GrandFather): # parent class
    def get_fathers_properties(self):
        print("owns a complex in Bangalore")


class Son(Father):  # child class
    def get_son_properties(self):
        print("owns a bike")
        

Harsha = Son()
Harsha.get_fathers_properties()
Harsha.get_grand_fathers_properties()
Harsha.get_son_properties()

# hybrid inheritance

class School:
    def info(self):
        print("School Info")

class Sports:
    def activity(self):
        print("Sports Activity")

class Student(School):
    def study(self):
        print("studying")
        
class Player(Student, Sports):
    pass