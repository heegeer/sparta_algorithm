finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    currnet_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[currnet_guess] == target:
            return True
        elif array[currnet_guess] < target:
            current_min = currnet_guess + 1
        else:
            current_max = currnet_guess - 1
        currnet_guess = (current_min + current_max) // 2
        # while문을 다시 한 번 돌기 전에 current_guess 값 업데이트 해주기

    return Flase

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)umbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


