"""
The intention of this script is to print all the possible permutations & combinations of
the string using itertools package.

"""

# import the combinations & permutation module from itertools
from itertools import combinations, permutations

# take the input from the console and fetch a space delimited output
# with "data" as the first and "n_pairs" as the second param
data, n_pair = input().split()


def get_permutations(string_input, num_element):
    print("PERMUTATIONS OF A STRING",
          *[''.join(i) for i in permutations(
              sorted(string_input), int(num_element))], sep="\n")


def get_combinations(string_input, num_element):
    print("COMBINATIONS OF A STRING",
          *[''.join(i) for i in combinations(
              sorted(string_input), int(num_element))], sep="\n")


if __name__ == '__main__':
    string, n_element = input().split()
    get_permutations(string, n_element)
    get_combinations(string, n_element)
