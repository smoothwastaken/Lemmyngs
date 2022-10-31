def printDocstring(f):
    def wrapper(*args, **kwargs):
        print(f.__doc__)
        return f
        
    return wrapper