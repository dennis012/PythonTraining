PI = 3.14

one = 1
two = 2
three = 3
print(PI * two)
print(one)
print(two)
print(three)
print(two * three)

Decimal = 1.1
print(Decimal)


def trial(a,b):
    Product = a * b
    return Product
a = 20
b = 20
output = trial(a,b)
print(output)

def division(number1,number2):
    division = number1/number2
    return division

a = 56
b = 8
result = division(a,b)
print(result)

def hello():
    print("I am a beginner")
hello()
hello()

def sumA(count):
    a = count + 1
    return a
a = sumA(2)
print(a)


def printmessage(message, ntimes=1):
    print(message * ntimes)

printmessage("Hello")
printmessage("Hello", 5)

num = 1
def func():
     num = 4
     print(num)
func()
print(num)