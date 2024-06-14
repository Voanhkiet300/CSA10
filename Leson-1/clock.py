class Counter():
    count = 0

    def __init__(self, name):
        self.name = name
    
    def tick(self):
        self.count += 1
        print(self.name, "\t", self.count)

    def reset(self):
        self.count = 0
        print("reset\t", self.count)

    def set_count(self, count):
        self.count = count
        return count

clock1 = Counter(name="clock1")
clock2 = Counter(name="clock2")
clock3 = Counter(name="clock3")

for i in range(3):
    clock1.tick()
clock1.reset()

print(clock1.set_count(10))