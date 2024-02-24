import random
def decorator(func):
    def mod_func(*args, **kwargs):
        print("Start of decorator.")
        func(*args, **kwargs)
        print("End of decorator.")
        print()
    return mod_func

@decorator

def factorial(n):
    l = [i for i in range(1,n+1)]
    product = 1
    for i in l:
        product *= i
    
    print(f"{n}! = {product}")

def random_number():
    print(random.randint(1, 10))

def exit():
    print("Bye for now.")

factorial(5)
random_number()
decorator(exit)()