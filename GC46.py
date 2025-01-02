def default_line():
    line(60)
def line(size):
    for length in range(1, size+1):
        print('-', end='')

mysize = int(input())

if mysize == -1:
    default_line()
else:
    line(mysize)
