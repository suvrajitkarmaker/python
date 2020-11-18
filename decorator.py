def check(func):
    def wrapper(a,b):
        if(b==0):
            return "Can not divide"
        return func(a,b)
    return wrapper

@check
def div(a, b):
    return a/b

print(div(5,0))
    