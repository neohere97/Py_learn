def pow(a,b):
    a_check = type(a) == int or type(a) == float
    b_check = type(b) == int or type(b) == float
    if(a_check and b_check):
        return a**b
    else:
        return "DTNS"
def mod(a,b):
    a_check = type(a) == int or type(a) == float
    b_check = type(b) == int or type(b) == float
    if(a_check and b_check):
        return a%b
    else:
        return "DTNS"
def add(a,b):
    a_check = type(a) == int or type(a) == float
    b_check = type(b) == int or type(b) == float
    if(a_check and b_check):
        return a+b
    else:
        return "DTNS"

