class animals:
    def __init__(self,name,colour,legs,habitant):
        self.name=name
        self.colour=colour
        self.legs=legs
        self.habitant=habitant
    def introduce(self):
        print(f"A {self.name} is {self.colour} and has {self.legs} legs and stays in a {self.habitant}")
    def color(self):
        print(self.colour)
Dog=animals("dog","black",4,"kennel")
impala=animals("impala","brown",4,"bush")
elephant=animals("elephant","grey",4,"bush")

elephant.introduce()
impala.color()


class people(animals):
    def __init__(self,name,colour,height,age):
        super().__init__(name,colour,legs,habitanat)
        self.height=height
        self.age=age
person1=people("Adrona","brown",112,19)
person2=people("Patience","brown",122,18)

person1.color()
