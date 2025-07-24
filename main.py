def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(text):
    contents = get_book_text(text)
    num_words = contents.split()

    return f"{len(num_words)} words found in the document"


def main(path_to_file):
    contents = get_book_text(path_to_file)
    print(contents)


##main("books/frankenstein.txt")
print(count_words("books/frankenstein.txt"))