# We are using the calculator app to explain how a function can be used as an input to another function

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(n1, n2, func):
    return func(n1,n2)

answer = calculate(4, 5, add)
print(answer)