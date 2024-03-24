from inspect import isgenerator

print('DZ23')


def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    while end:
        end -= 1
        yield begin
        begin = func(begin)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

print('Thank you for using')