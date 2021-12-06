"""
The intention of this script is to print all the possible permutations & combinations of
the string using itertools package.

"""

# import the combinations & permutation module from itertools
from itertools import combinations, permutations


def get_permutations(string_input, num_element):
    print("PERMUTATIONS OF A STRING",
          *[''.join(i) for i in permutations(
              sorted(string_input), int(num_element))], sep="\n")


def get_combinations(string_input, num_element):
    print("COMBINATIONS OF A STRING",
          *[''.join(i) for i in combinations(
              sorted(string_input), int(num_element))], sep="\n")


if __name__ == '__main__':
    # take the input from the console and fetch a space
    # delimited output with "string" as the first
    # and "n_element" as the second param.

    string, n_element = input().split()

    """
        e.g. HACK 2 will have the "string" as HACK & 2 
        as the "n_element", hence the permutations will be
        AC, AH, AK, CA, CH, CK, HA, HC, HK, KA, KC, KH
    """
    get_permutations(string, n_element)

    """
            e.g. HACK 2 will have the "string" as HACK & 2 
            as the "n_element" hence the  will be 
            AC, AH, AK, CH, CK, HK
    """

    get_combinations(string, n_element)
