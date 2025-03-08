def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

if __name__ == "__main__":
    main()
