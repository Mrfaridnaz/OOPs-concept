class Pet:
    def __init__(self, name, breed, speak):
        self.name = name
        self.breed = breed
        self.speak = speak

    def sound(self):
        return f"{self.name} says {self.speak}! and breed is {self.breed}"

pet1 = Pet("Buddy", "Golden Retriever", "Woh")
pet2 = Pet("Monk","white", "Meow")
print(pet1.sound())
print(pet2.sound())
