formater = "{} {} {} {}"

print(formater.format(1,2,3,4))
#this one is same as the last ont
print(formater.format("one","two","three","four",end="SGmez"))
#this one should output true false false true
print(formater.format(True,False,False,True))
#this one should output 12 curly brackets
print(formater.format(formater,formater,formater,formater))
#this is the last one
print(formater.format(
    "I wond",
    "and",
    "you know",
    "it"
))

st1 = "I am a string"
st2 = "I am another string"

st3 = f"{st1} {st2}"

st4 = "{} {}".format(st1,st2)

print(st3,end='\n')
print(st4)

