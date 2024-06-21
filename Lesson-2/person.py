class Person:
    def __init__(self, name, age) -> None:
        # print(self.__dir__())
        self.name = name
        self.age = age

    # override
    def __str__(self):
        return "Your name is: " + self.name

# person1 = Person("A", 23)
# person2 = Person("B", 22)
# print(person1.__str__())
# print(person1.__eq__(person2))


class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)


student1 = Student("A", 12)
print(student1.__str__())