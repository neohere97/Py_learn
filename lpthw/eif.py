people = 30
cars = 40
trucks  = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("we cant decide")


if trucks > cars:
    print("That's too many trucks")
elif trucks < cars :
    print("maybe we can take the trucks")
else:
    print("We still cant decide")


if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine let's stay home then")

    
