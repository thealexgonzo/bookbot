def get_num_words(contents):
    num_words = contents.split()
    return f"{len(num_words)} words found in the document"

def count_characters(book):
    my_dict = {}

    for char in book:
        if(char.lower() in my_dict):
            my_dict[char.lower()] += 1
        else:
            my_dict[char.lower()] = 1
    
    return my_dict