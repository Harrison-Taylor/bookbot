def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    length = words(file_contents)
    number_of_letters = characters(file_contents) 
    report = char_count_report(number_of_letters)
    
    print("Report of Frankenstein")
    print(f"{length} words found in the book")
    print(report)
    for letter in report:
        print(f"The '{letter["char"]}' was found {letter["num"]} times")

def words(text):
    split = text.split()
    length = len(split)
    return length

def characters(text):
    char_dictionary = {}
    lowered_string = text.lower()
    lowered_letters = list(lowered_string)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in alphabet:
        count = 0
        for character in lowered_letters:
            if character == letter:
                count += 1
        char_dictionary[letter] = count
    return char_dictionary

def sort_on(dict):
    return dict["num"]

def char_count_report(character_dictionary):
    sorted_characters = []
    for character in character_dictionary:
        sorted_characters.append({"char": character, "num": character_dictionary[character]})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters

main()
