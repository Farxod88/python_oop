
class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def hello(self):
        print('hello')

    def report(self):
        print(f'I am {self.f_name}, {self.l_name}')
# a = Person('Farxod','Rasulov')
# print(a.report())

class Agent(Person):

    def __init__(self,f_name, l_name, seckreet):
        Person.__init__(self)
    def reveal(self, code):
        if code = '007'

            print('Bond', 'Jems Bond')
        else
            self.report()