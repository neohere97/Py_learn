from sys import argv
from os.path import exists

def print_two(*args):
    arg1,arg2 = args
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin")


print_two("drg","dfg")
print_two_again("hfgf","juf")
print_one("dfhgd")
print_none()