def count_letters(words):
    letters_in_words = []

    for word in words:
        letters_in_words.append(int(len(word)))

    return letters_in_words

def calc_average(letters_in_words):
    return round(sum(letters_in_words) / len(letters_in_words))

def find_closest_index(list_of_nums, num):
    diffs = [abs(num - number) for number in list_of_nums]
    smallest = min(diffs)

    return diffs.index(smallest)