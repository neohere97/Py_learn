from sys import argv


script, user_name = argv
promt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}")

likes = input(promt)

print(f"where do you live {user_name}")
lives= input(promt)

print("What kind of computer yoy have?")
computer = input(promt)

print(f"""Alright, so you said {likes} abot liking me.  
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.""")
