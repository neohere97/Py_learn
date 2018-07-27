from sys import argv
from os.path import exists

script, fname = argv

def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count, f.readline())

current_file = open(fname)

print("Here is the whole file")

print_all(current_file)

rewind(current_file)

i=1
print_a_line(i,current_file)
print_a_line(i+1,current_file)
print_a_line(i+2,current_file)
    
