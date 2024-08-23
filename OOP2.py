class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof! and breed is {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Monk","white")
print(dog.bark())
print(dog2.bark())
