class Animal:
    # member variable - attribute
    age = 1

    # ham khoi tao
    def __init__(self, name):
        self.name = name

    # method
    def talk(self):
        print("aa")


cuu = Animal(name="abc")
print(cuu.name)
cuu.talk()