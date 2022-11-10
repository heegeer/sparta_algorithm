input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multipliy_sum = 0
    for num in array:
        if num <= 1 or multipliy_sum <= 1:
            multipliy_sum += num
        else:
            multipliy_sum *= num

    return multipliy_sum


result = find_max_plus_or_multiply(input)
print(result)