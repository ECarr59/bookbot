def main():
    #opens a file from the books directory and saves the text as file_contents string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    f.close()

    print(file_contents)

    count = word_count(file_contents)

    print(count)

#takes a string and returns the word count
def word_count(book_text):
    count = len(book_text.split())
    return count





main()