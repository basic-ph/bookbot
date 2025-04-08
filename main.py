import sys

from stats import count_words, count_chars, get_sorted_chars


def get_book_text(file_path: str):
    with open(file_path) as f:
        file_content = f.read()
        return file_content


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_chars(text)
    sorted_chars = get_sorted_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


main()
