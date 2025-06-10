import sys

from stats import count_chars, count_words, sort_freq


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def _check_args(arg_list):
    if len(arg_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return arg_list[1]


def main():
    book_path = _check_args(sys.argv)

    book_text = get_book_text(book_path)

    num_words = count_words(book_text)

    char_freq = count_chars(book_text)

    sorted_freq = sort_freq(char_freq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch_info in sorted_freq:
        if ch_info["char"].isalpha():
            print(f"{ch_info['char']}: {ch_info['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    main()
