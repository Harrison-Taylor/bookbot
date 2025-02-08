def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    length = words(file_contents)
    number_of_letters = characters(file_contents)    
    return print(length), print(number_of_letters)

def words(text):
    split = text.split()
    length = len(split)
    return length

def characters(text):
    char_dictionary = {}
    lowered_string = text.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        count = 0
        for character in lowered_string:
            if character == letter:
                count += 0
    char_dictionary[letter] = count
    return char_dictionary