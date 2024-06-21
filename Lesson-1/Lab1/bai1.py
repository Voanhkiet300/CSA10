class Employee:
    def __init__(self, fullname, position) -> None:
        self.fullname = fullname
        self.position = position
    
    def say_hi(self):
        print("Hello", self.fullname)

    def tell_position(self):
        print("I am", self.position)

emp1 = Employee("Nguyen Van A", "Dev")
emp2 = Employee("Nguyen Van B", "Team leader")

emp1.say_hi()
emp2.tell_position()