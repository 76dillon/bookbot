def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    char_list = []
    for key, value in dict.items():
        new_dict = {'char' : key, 'count' : value}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    

def get_num_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def count_char(book_text):
    book_text = book_text.replace('\n', ' ') #Replace '\n' with spaces
    char_dict = {}
    for char in book_text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict