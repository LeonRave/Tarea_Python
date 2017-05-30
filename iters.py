import math
#Generador
def fibon(n):
	a=b=1
	for i in range(n):
		yield a
		a, b = b, a + b

my_gen = fibon(4)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


root = lambda x: math.sqrt(x)
print(root(10))

