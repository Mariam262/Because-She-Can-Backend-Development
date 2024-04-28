class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
            print("hello")

p=Person("ali")
print(p.name)
p.talk()