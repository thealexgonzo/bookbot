def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

from stats import count_words

def main(path_to_file):
    contents = get_book_text(path_to_file)
    print(contents)


main("books/frankenstein.txt")
print(count_words("books/frankenstein.txt"))