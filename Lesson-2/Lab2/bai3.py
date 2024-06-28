class Square:

    def __init__(self, length) -> None:
        self.length = length

    def cal_area(self):
        return self.length**2
    

class Cube(Square):
    def __init__(self, length) -> None:
        super().__init__(length)

    def cal_area(self):
        return super().cal_area() * 6

    def cal_volume(self):
        return self.length**3




square = Square(2)
print('Square area:', square.cal_area())


cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())
