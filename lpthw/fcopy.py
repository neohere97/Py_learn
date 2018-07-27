from sys import argv 
from os.path import exists

script, fname, f2name = argv

print(exists(fname))
print(exists(f2name))

f1 = open(fname,'r')
f2 = open(f2name,'r')
tx1 = f1.read()
f1.close()
f1 = open(fname,'w')
f1.truncate()

#for some reason r+ and w+ do not seem to work all that well

tx2 = f2.read()
f2.close()
f2 = open(f2name,'w')
f2.truncate()

print(tx1 + '\n' + tx2)

f1.write(tx2)

f2.write(tx1)

f1.close()
f2.close()

print("The file have been interchanged")