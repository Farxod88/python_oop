
class BaseClass:
    def call_me1(self):
        print('Metod call_me1() BaseClass')
class LeftSuclass(BaseClass):
    def call_me2(self):
        print('Metod call_me2() LeftSuclass')
class RightSubclass(BaseClass):
    def call_me1(self):
        print('Metod call_me1() RightSubclass')
    def call_me2(self):
        print('Metod call_me2() RightSubclass')
    def call_me3(self):
        print('Metod call_me3() RightSubclass')
    def call_me4(self):
        print('Metod call_me4() RightSubclass')
class Subclass(LeftSuclass, RightSubclass):
    def call_me4(self):
        print('Metod call_me4() Subclass')


a1=Subclass()
a1.call_me1()
# a1.call_me2()
# a1.call_me3()
# a1.call_me4()
