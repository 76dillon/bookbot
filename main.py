from stats import get_num_words
from stats import count_char
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    #Count number of words in text
    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print("Invalid path to tile.")
        sys.exit(1)
    word_count = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing words found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    #Count number of each character type
    char_dict = count_char(book_text)
    #Return sorted character count list from greatest to least frequemt
    char_list = sort_dict(char_dict)
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
main()