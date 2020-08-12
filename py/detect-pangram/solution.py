import string
import re


def is_pangram(s):
    remove_non_alpha = re.sub('\W|\d', '', s.lower())

    unique_alpha = set(remove_non_alpha)

    return True if len(unique_alpha) == 26 else False


# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))
