import morepr

sentence = "All good this come to those who wait."

words = morepr.break_words(sentence)
print(words)
sorted_words = morepr.sort_words(words)
print(sorted_words)
morepr.print_first_word(words)
morepr.print_last_word(words)
print(words)
morepr.print_first_word(sorted_words)
morepr.print_last_word(sorted_words)
print(sorted_words)
sorted_words = morepr.sort_sentence(sentence)
print(sorted_words)
morepr.print_first_and_last(sentence)
morepr.print_first_and_last_sorted(sentence)
