str1 = "Practice makes perfect"
str2 = "perfect makes practice"


def is_anagram(str_1, str_2):
    str_1 = str_1.lower().replace(" ", "")  # convert to lower
    str_2 = str_2.lower().replace(" ", "")  # and remove spaces

    if len(str_1) != len(str_2):
        return False

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dict_1 = dict.fromkeys(list(alphabet), 0)  # creating keys from the
    # alphabet list
    dict_2 = dict.fromkeys(list(alphabet), 0)

    # we will loop each string and update the hash table value

    for i in range(len(str_1)):
        dict_1[str_1[i]] += 1  # we are passing the string character to the key and incrementing the value.
        dict_2[str_2[i]] += 1

    return dict_1 == dict_2


print(is_anagram(str1, str2))
