
import sys
from stats import count_words, count_characters, sort_character_counts


def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    command_line_arguments = sys.argv
    if not len(command_line_arguments) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text_path = command_line_arguments[1]
    book_text = get_book_text(text_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_character_counts = sort_character_counts(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in sorted_character_counts:
        if not entry["char"].isalpha():
            continue
        print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")

main()
