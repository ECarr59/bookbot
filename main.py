def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    f.close()

    print(file_contents)

    word_count(file_contents)

def word_count(book_text):
    count = len(book_text.split())
    print(count)





main()