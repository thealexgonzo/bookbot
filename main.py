from stats import get_num_words

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def main(path_to_file):
    book = get_book_text(path_to_file)
    
    word_count = get_num_words(book)

    print(word_count)


main("books/frankenstein.txt")
