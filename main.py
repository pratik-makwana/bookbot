def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    text =  get_book_text(book_path)
    print(text)


if __name__ == "__main__":
    main()