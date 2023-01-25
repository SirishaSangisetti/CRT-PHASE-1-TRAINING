class Animal:
    def speak(self):
        print("different types:")
    def colour(self):
        print("different colour:")
class Dog(Animal):
    def speak(self):
        print("Bow Bow:")
    def colour(self):
        print("black colour:")
class Cow(Animal):
    def speak(self):
        print("Amba Amba:")
    def colour(self):
        print("white colour:")
class Cat(Animal):
    def speak(self):
        print("Meow Meow:")
    def colour(self):
        print("brown colour:")
obj=Cow()
print(obj.speak())
print(obj.colour())
