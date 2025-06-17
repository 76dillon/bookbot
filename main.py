def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

main()