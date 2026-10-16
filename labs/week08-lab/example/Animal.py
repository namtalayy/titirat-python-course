# Parent class (Base class)
class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class)
class Dog(Animal):
    def __init__(self, name, breed):
<<<<<<< HEAD
        super().__init__(name, "Canine")  # Call parent constructor # super พูดถึงแม่
        self.breed = breed
    
    # Method overriding ได้รับการถ่ายถอดจากแม่
=======
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
    
    # Method overriding
>>>>>>> upstream/main
    def make_sound(self):
        print(f"{self.name} barks: Woof!")
    
    # New method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} meows: Meow!")
    
    def climb_tree(self):
        print(f"{self.name} is climbing a tree")

# Usage
dog = Dog("Max", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

<<<<<<< HEAD
dog.eat()        # Inherited method สามารถต่อยอด code ของเราหรือคนอื่นได้
=======
dog.eat()        # Inherited method
>>>>>>> upstream/main
dog.make_sound() # Overridden method
dog.fetch()      # Dog-specific method

cat.make_sound() # Overridden method
cat.climb_tree() # Cat-specific method