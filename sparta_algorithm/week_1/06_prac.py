input = "abadaba"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        # 수정 부분
        # alphabet_occurrence = alphabet_occurrence_array[index]
        # if alphabet_occurrence == 1:
        if alphabet_occurrence_array[index] == 1:
            not_repeating_character_array.append(chr(index + ord('a')))

    for char in string:
        if char in not_repeating_character_array:
            return char

    else:
        return "_"


result = find_not_repeating_character(input)
print(result)