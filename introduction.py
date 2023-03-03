# class Person:
#     def __init__(self, jinsi, ismi, yoshi, kasibi, ishjoyi):  # metod
#         self.jins=jinsi
#         self.ism=ismi
#         self.yosh=yoshi
#         self.kasib=kasibi
#         self.ishjoyi=ishjoyi
#
#
# farxod = Person('Erkak', 'Farxod', '34', 'progmammist' , 'IT Park') # instinslar
# print(f'Mening ismim {farxod.ism}\n jinsim {farxod.jins}\n yoshim {farxod.yosh}\n kasibim {farxod.kasib}\n ish joyim {farxod.ishjoyi}\n')


class Car:
    def __init__(self, model, color, probeg):
        self.color = color
        self.probeg = probeg
        self.model = model

    def __str__(self):
        return f'Model {self.model}\nColor {self.color}\nProbeg {self.probeg}\n'

    def drive(self, mile):
        self.probeg += mile

    def get_mileage(self):
        return self.probeg



c1 = Car('BMW', 'Red', 2550) #instins
c2 = Car('malibu', 'black', 3000)  #instins
c1.drive(100)

# for car in (c1, c2):
#     # print(f'Model{c1}, Model{c2}')
#     print(car)

print(c1.get_mileage())


# class Car()
