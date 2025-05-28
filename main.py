import sys
from stats import get_words_in_string, get_characters_in_string, get_sorted_char_dict_list

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
        return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    # print(book_text)
    word_count = get_words_in_string(book_text)
    print(f"{word_count} words found in the document")
    char_dict = get_characters_in_string(book_text)
    char_list_dict = get_sorted_char_dict_list(char_dict)

    # Printing report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_list_dict:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()