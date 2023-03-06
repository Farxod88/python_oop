class Counter:
    def __init__(self, start, stop):
        self.start=start
        self.stop = stop

    def increment(self):
        self.start+=1

    def get(self):
        if self.start<=self.stop:
         return  self.start
        else:
            print(f'Maximal value is reached')


c = Counter(start=10, stop=15)
print(c.increment())
print(c.get())
print(c.increment())
print(c.get())
print(c.increment())
print(c.get())
print(c.increment())
print(c.get())
print(c.increment())
print(c.get())
print(c.increment())
print(c.get())
print(c.increment())
print(c.get())