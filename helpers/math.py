def count_letters(words):
    return [len(word) for word in words]


def calc_average(letters_in_words):
    return round(sum(letters_in_words) / len(letters_in_words))


def find_closest_index(list_of_nums, average):
    diffs = [abs(average - number) for number in list_of_nums]
    smallest = min(diffs)

    return diffs.index(smallest)
