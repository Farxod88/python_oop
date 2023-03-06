
class Field:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
       return self.__value



    def set__value(self, name):
       self.__value=name



a1=Field('Jonh Smit')

# print(a1.get_value())
a1.set__value('Bob')
print(a1.get_value())
