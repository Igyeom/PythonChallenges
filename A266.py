from matplotlib.pyplot import ylabel, plot, show, xlabel, title
import math

x = [2, 4, 6, 8, 10, 12]
log = [math.log2(i) for i in x]
quad = [i*i for i in x]
expo = [2**i for i in x]
factorial = [math.factorial(i) for i in x]

plot(x, log, 'b')
plot(x, quad, 'g')
plot(x, log, 'y')
plot(x, expo, 'o')
plot(x, factorial, 'r') # might have to comment expo and factorial out to actually see the graph lol
xlabel('Inputs')
ylabel('Steps')
title('Constant Complexity')
show()
