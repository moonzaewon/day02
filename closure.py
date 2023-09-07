def counter(count = 0):
    def increase(c = 1):
        nonlocal count
        count += c
        return count
    return increase

myCounter = counter()
yourCounter = counter()
print("myCounter", myCounter())
print("yourCounter", yourCounter())
print("myCounter", myCounter())
print("yourCounter", yourCounter())
print("myCounter", myCounter())
print("yourCounter", yourCounter())
del(myCounter)
del yourCounter