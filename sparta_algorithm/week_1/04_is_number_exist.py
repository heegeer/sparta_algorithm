input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array:
        if number == num:
            return True
        else:
            return False


result = is_number_exist(7, input)
print(result)