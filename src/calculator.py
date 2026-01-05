def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0 :
        raise ValueError('can not divide by zero')
    return a / b


if __name__ == "__main__":
    print("Add:",add(10, 5))
    print("Substract:",subtract(20, 7))
    print("Multiply:",multiply(9, 3))
    print("Division:",divide(7, 0))



