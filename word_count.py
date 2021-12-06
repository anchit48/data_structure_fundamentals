# The intention of this script is to count the words in a string
# using collections counter utility and print the word with it's
# corresponding freq count


# import collections Counter class
from collections import Counter, OrderedDict


def get_word_count(name):
    """

    :param name: name
    :return: OrderedDict
    """
    return OrderedDict(Counter(name.split()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentence = input()

    """
    e.g. i love paris paris is in france france is in europe
    will yield following output:
    OrderedDict([('i', 1), ('love', 1), ('paris', 2), ('is', 2), ('in', 2),
    ('france', 2), ('europe', 1)])
    """
    wc_dist = get_word_count(sentence)
    print(wc_dist)
