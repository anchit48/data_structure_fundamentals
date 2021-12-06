"""
This process will generate N-GRAM from a string input & freq as an o/p
N-GRAM will have "_" as delimiters and int as the freq
"""

# import the Counter utility from collections

from collections import Counter, OrderedDict


def get_n_gram(input_string, n_gram):
    """

    :type input_string: str
    """
    ngram_ = ['_'.join(input_string.split()[j:j+n_gram])
              for j in range(0, len(input_string.split())-1)]
    return Counter(ngram_)


if __name__ == '__main__':
    # take the input from the console and fetch a pipe
    # delimited output with "string" as the first
    # and "n_gram" as the second param.

    input_string, n_gram = input().split('|')

    """
            e.g. "anchit saxena is working in XYZ|2" passed as pipe sep
            input with 2 as the n_gram len
            
            Counter({'anchit_saxena': 1, 'saxena_is': 1, 'is_working': 1, 'working_in': 1, 'in_ZYZ': 1})
    """
    n_gram_count = get_n_gram(input_string, int(n_gram))

    print(n_gram_count)
