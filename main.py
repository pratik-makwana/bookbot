import sys
from stats import get_num_words, get_chars_count, char_dict_to_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, sorted_list):
    print(
        f"============ BOOKBOT ============\n Analyzing book found at {book_path}...\n"
        f" ----------- Word Count ----------\n Found {num_words} total words\n"
        f" --------- Character Count -------\n"
    )  
    for items in sorted_list:
        dict_key = list(items.keys())[0]
        dict_value = list(items.values())[0]
        print(f"{dict_key}: {dict_value}")

    print("============= END ===============")  



def main():
    try:
        book_path = sys.argv[1]

    except IndexError:
        print("Usage: python3 main.py <path_to_book>")   
        sys.exit(1)
        
    else:

        text =  get_book_text(book_path)
        num_words = get_num_words(text)
        chars_count = get_chars_count(text)
        char_sorted_list = char_dict_to_sorted_list(chars_count)
        print_report(book_path=book_path, num_words=num_words, sorted_list=char_sorted_list)

if __name__ == "__main__":
    main()