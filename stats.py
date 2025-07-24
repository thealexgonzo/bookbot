def count_words(text):
    contents = get_book_text(text)
    num_words = contents.split()

    return f"{len(num_words)} words found in the document"