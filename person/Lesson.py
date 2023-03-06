def phone_num(func):
    def wapper(*args):
        func(args)
        # a = func(args)
        # return '+998' + str(a)
        print(f'+998{func(*args)}')
        return

    return wapper


@phone_num
def phone(numb):
    return numb


print(phone(998033968))
