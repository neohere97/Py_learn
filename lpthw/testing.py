from sys import argv

script, fname = argv

f1 = open(fname, "r", encoding = "utf-8")

def selff():
    l = f1.readline()

    if l:
        print_line(l)

def print_line(ll):
    print(ll)
    selff()

selff()
      


