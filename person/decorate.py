# HW1
def add_one():
    return add_one()

def plus_one(number):
    return number + 1

add_one = plus_one

print(add_one(7))

# HW2
def uppercase_dec(func):
    print(f'Hello Farxod')
    print(f'{func()}'.upper())
@uppercase_dec
def say_hi():
    return 'hello there'
print(say_hi)
