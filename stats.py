
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

def sort_character_counts(character_count_dictionary):
    sorted_list = [ { "char" : k, "num":  character_count_dictionary[k]} for k in character_count_dictionary]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
