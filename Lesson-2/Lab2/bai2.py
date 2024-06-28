class MathList:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def __add__(self, num):
        return MathList([x + num for x in self.values])

    def __sub__(self, num):
        return MathList([x - num for x in self.values])
    


values = MathList([1, 2, 3, 4, 5])
print(values)  # [1, 2, 3, 4, 5]

result = values + 2
print(result)  # [3, 4, 5, 6, 7]
