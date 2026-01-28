class Animal():
    def __init__(self, name):
        self.name=name
    def speak(self):
        print(f"{self.name} can speak")
    def eat(self):
        print(f"{self.name} can eat")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color=color
    def about(self):
        print(f"{self.name} is of {self.color} color")
    
dog = Dog("sheru", "black")
dog.eat()
dog.about()