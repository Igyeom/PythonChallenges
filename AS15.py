def hello():
    print('Hello World')


def add(x, y):
    print(f'arguments are {x} and {y}')
    return x + y

hello()
sum = add(10, 5)
print(f'sum is {sum}')

def hello(year=2019):
    print(f'Hello World {year}')
 
 
hello(2020)
hello()

def odd_even_checker(i):
    if i % 2 == 0:
        return 'even'
    else:
        return 'odd'
 
 
print(odd_even_checker(20))
print(odd_even_checker(15))

def return_odd_ints(i):
    x = 1
    while x <= i:
        yield x
        x += 2

output = return_odd_ints(10)
for out in output:
    print(out)

def add(x, y, *args, **kwargs):
    sum = x + y
    for a in args:
        sum += a
 
    for k, v in kwargs.items():
        sum += v
    return sum
 
 
total = add(1, 2, *(3, 4), **{"k1": 5, "k2": 6})
print(total)

def fibonacci_numbers_at_index(count):
    if count <= 1:
        return count
    else:
        return fibonacci_numbers_at_index(count - 1) + fibonacci_numbers_at_index(count - 2)
 
 
count = 5
i = 1
while i <= count:
    print(fibonacci_numbers_at_index(i))
    i += 1

def foo():
    pass


print(type(foo))

class Data:
    def foo(self):
        print('foo method')
 
 
def foo():
    print('foo function')


foo()

d = Data()
d.foo()

print(type(foo))
print(type(d.foo))

def square(x):
    return x * x
 
f_square = lambda x: x * x
 
print(square(10))
print(f_square(10))
