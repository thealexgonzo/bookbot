from stats import get_num_words
from stats import count_characters
from stats import sort_on

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def main(path_to_file):
    book = get_book_text(path_to_file)
    word_count = get_num_words(book)
    char_count = count_characters(book)
    sorted_chars = sort_on(char_count)

    print("============ BOOKBOT ============"
          + f"\nAnalyzing book found at {path_to_file}..."
          + "\n----------- Word Count ----------"
          + f"\n{word_count}"
          + "\n--------- Character Count -------")
    
    for i in range(0, len(sorted_chars)):
        print(f"{sorted_chars[i]["char"]}: {sorted_chars[i]["num"]}")
    
    print("\n============= END ===============")

    


main("books/frankenstein.txt")
