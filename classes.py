"""
x=input ("Enter Name: ")
print()
age=int(input("Enter Age: "))
iq = 2*age

print()
print(x +" is " + str(age) + " years old and has an IQ of: " + str(iq))
print()
print(f"{x} is {age} years old and has an IQ of: {iq}")
"""


class Animal():
    def __init__(self, animal_name, legs, sound, tails, colour):
        self.legs = legs
        self.sound = sound
        self.tails = tails
        self.colour = colour
        self.animal_name = animal_name

    def introduce(self):
        print(f"A {self.animal_name} has {self.legs} legs, it {self.sound}, and it has {self.tails} tails, and it is {self.colour}")
        
    def speak(self):
        sound = input("Enter sound: ")
        print(f"The dog {sound}.")

class Person(Animal):
    def __init__(self, animal_name, legs, sound, tails, colour, education):
        super().__init__(animal_name, legs, sound, tails, colour)
        self.education = education
    

    
dog = Animal("Dog", 14, "barks", 1, "brown")
dog.introduce()
dog.speak()
print()
print()

cat = Animal("Cat", 4, "meows", 1, "black")
cat.introduce()


kim = Person("Kim", 2, "Luganda", 0, "dark-skined", "University")
kim.introduce()
