from stats import get_num_words, get_chars_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    text =  get_book_text(book_path)
    num_words = get_num_words(text)
    words_count = get_chars_count(text)
    print(f"{num_words} words found in the document")
    print(words_count)

if __name__ == "__main__":
    main()