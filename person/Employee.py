
class Employee:

    def __init__(self, fname, lname,gmail, pay):
        self.fname=fname
        self.lname=lname
        self.fullname=fname+lname
        self.gmail=gmail
        self.pay=pay

        print(f'{self.fname}, {self.lname}, {self.fullname},{self.gmail}, {self.pay}')




ishchi=Employee('Jems', 'bond', '@bond007', 4500)