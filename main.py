def main():
    #opens a file from the books directory and saves the text as file_contents string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    f.close()

    print("--- Begin report of books/frankenstein.txt ---")

    count = word_count(file_contents)

    print(f"{count} words found in the document")

    alphabet = letter_count(file_contents)

    for letter in alphabet:
        times = alphabet[letter]
        print(f"The '{letter}' character was found {times} times")

#takes a string and returns the word count
def word_count(book_text):
    count = len(book_text.split())
    return count

#takes a string and returns a dictonary that contains the number of times each letter appears within the string
def letter_count(book_text):
    lower_case = book_text.lower()
    #initializes the diconary with each letter of the alphabet and sets the initial value to 0
    alphabet = {'a': 0, 'b': 0, 'c':0, 'd': 0, 'e': 0, 'f':0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for letter in lower_case:
        if letter.isalpha() == True:
            alphabet[letter] += 1

    return alphabet


main()