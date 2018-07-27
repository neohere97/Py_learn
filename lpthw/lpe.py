print("Let's practice everything")
print("\n newlines and \t tabs.")

poem = """
\tdfsdfgsdfsdf
asdfasdfas
asfdasdfa\nasdfa
asdfasdf
asdfasd
asdfasdf
\n\t\t sdfa."""

print("----------")
print(poem)
print("----------")

five =  10-2+3-6

print(f"this should be {five}")

def secret_formula(started):
    jelly_beans = started *500
    jars = jelly_beans /1000
    crates = jars/100
    return jelly_beans, jars,crates

start_point = 10000

beans, jars, crates = secret_formula(start_point)

print("with a starting point of : {}".format(start_point))

print(f"we have {beans} beans {jars} jars {crates} crates")

start_point = start_point / 10

print("we can also do that this way :")

formula = secret_formula(start_point)
# the bloody star is not a pointer! ATTENTION the star is used ot unpack the variable into its tuples
# the '**' is the same but can use dictionary and can upacked named stuff
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
