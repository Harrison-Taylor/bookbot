def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    length = words(file_contents)    
    return print(length)

def words(text):
    split = text.split()
    length = len(split)
    return length
main()