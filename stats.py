
def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text):
    normalized_text = text.lower()
    count_results = { }
    for c in normalized_text:
        if c not in count_results:
            count_results[c] = 0
        count_results[c] += 1
    return count_results
