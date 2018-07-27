from sys import argv

script, filen = argv

op = open(filen)
print(op.read())
i=1
op.close()
print("Hahaha now nothing is there")

# So w is a modifier and r stands for read and w stands for write and a for append
# w+ r+ and a+ also open the file in multiple modes
op = open(filen,'w')

op.truncate()
op.write("This is the new text")



