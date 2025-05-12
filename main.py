from stats import get_num_words
from stats import get_count_letter
from stats import sorting

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    # Get word count
    word_count = get_num_words(text)

    # Get character counts
    dictionary = get_count_letter(text)

    # Get sorted list of character dictionaries
    dictionary_two = sorting(dictionary)

    # Print the report
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Print each character and its count (alphabetical characters only)
    for char_dict in dictionary_two:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    
    print ("============= END ===============")


main()




    
