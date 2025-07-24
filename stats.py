def get_num_words(contents):
    num_words = contents.split()
    return f"Found {len(num_words)} total words"

def count_characters(book):
    my_dict = {}

    for char in book:
        if(char.lower() in my_dict):
            my_dict[char.lower()] += 1
        else:
            my_dict[char.lower()] = 1
    
    return my_dict

def sort_on(items):
    
    dict_list = []
    my_max = float('-inf')

    for item in items:
        if(item.isalpha()):
            if(items[item] > my_max):
                dict_list.insert(0, {"char": item, "num": items[item]})
                my_max = items[item]
            else:
                dict_list.append({"char": item, "num": items[item]})


    return dict_list

