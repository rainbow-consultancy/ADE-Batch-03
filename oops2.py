# poly-morphism


class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"
    
    # def speak(self):
    #     return "Cat Meow"
    
    
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

# animal_sound(dog)
# animal_sound(cat)

# Abstraction 

from abc import ABC, abstractmethod


class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius**2
    
    def get_area(self, radius):
        return 3.14 * radius**2

# cir = Circle()
# print(cir.get_area(10))

# rec  = Rectangle()
# print(rec.area(10, 12))


# super()

class Animal():
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog Barks!")

dog = Dog()
dog.sound()