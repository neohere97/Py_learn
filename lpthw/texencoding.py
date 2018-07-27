from sys import *

script, input_enc, error = argv

def main(language_file,encoding, errors):
    line = language_file.readline()

    if line :
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # The below line just stripes the lines of their ending \n's . I dont know why it's being done. but moving on
    next_lang = line.strip()
    raw_bytes =  next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt",encoding="utf-8")

main(languages, input_enc , error)
    