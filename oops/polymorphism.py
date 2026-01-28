class Animal():
    def speak(self):
        print("Can speak")

class Dog(Animal):
    def speak(self):
        print("can bark")

animal = Animal()
dog = Dog()
dog.speak()
