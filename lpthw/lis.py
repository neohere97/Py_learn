from sys import *
# for number in a:
#     print(f"I am {number}")
script, fname = argv

a = []
def load():
    check = False
    i=0
    f1 = open(fname,'r+')
    while check != True:
        k = f1.readline()
        
        if k != '':
             a.append(k)
             i += 1
        else :
            check = True
    f1.close()

def display_elements():
    for i in range(0,len(a)):
        print(f"The list element is {a[i]}")
        
    add()

def add():
   
    f1 = open(fname,'a+')
    k = input("type an element you want to add, or press exit to exit \n ")
    if(k == "exit"):
        exit(0)#exit(0) is considered as a graceful exit without any error

    else :
        a.append(k)
        f1.write(k+'\n')
        display_elements()
    f1.close()

def start():
   
    load()
    display_elements()

start()

exec("print("hello")")





 

