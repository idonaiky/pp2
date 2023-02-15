from itertools import permutations
def find_permutations(str):
    char_list = [str[i] for i in range(0, len(str))]
    char_list.sort()
    prms = permutations(char_list)
    for permutation in prms:
        print(permutation)
find_permutations("bcad")