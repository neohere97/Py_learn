class Song(object):
    def __init__(self,lyrics,test):
        self.lyrics = lyrics
        self.test = test

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def printnum(self):
        print(self.test)


happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"],37)

bulls_on_parade = Song(["they rally around the family","With pocket full of shells"],84)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

hello = Song(22,33)

print("*"*10,end = "\n") #This stuff is weird man weird 
happy_bday.printnum()    #So when the init function is defined to receive more than one parameters 
                           #You have to send in so many parameters and there is no way around that
hello.printnum()         # I am understand the mechanics of it but I still don't feel like I have an 
                         #Intuitive understanding of it
print("*"*10,end = "\n")



