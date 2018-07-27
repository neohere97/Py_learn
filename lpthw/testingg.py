from morepr import *

sentence = "All good things come to those who wait"

print(break_words(sentence))

print(sort_words(break_words(sentence)))

print(print_first_and_last(break_words(sentence)))

print(print_first_and_last(sort_words(break_words(sentence))))
