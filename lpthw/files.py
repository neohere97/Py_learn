from sys import argv
script, filename = argv

#looks like the variable txt just points to the locaiton 
#of the text file
# So this below line opens the file
txt  = open(filename)

print(f"Here's your file {filename}:")
#This below code seem uses the read funciton and the 
#read function seems to be a blocking type
#let's do a quick test
print("Text pretext",end="\n")
print(txt.read())
print("post text")
# Confirmed it is a blocking type method and a 29000 likes text takes noticible fraciton of time.
print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

