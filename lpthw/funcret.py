

def add(a,b):
    print(f"Addming {a} + {b}", end='\n\n')
    return a+b

def subtract(a,b):
    print(f"Subtracting {a} - {b}",end='\n\n')
    return a-b

def multiply(a,b):
    print(f"multiplying {a} * {b}",end='\n\n')
    return a*b

def power(a,b):
    print(f"{a} to the power {b}",end='\n\n')
    return pow(a,b)


print(multiply(5,67))

print(power(2,3))

print(subtract(6,4))

print(add(22,65))

print(power(add(3,6),subtract(3,0)))

 