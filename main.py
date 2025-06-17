from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")

main()