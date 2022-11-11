numbers = [2, 3, 1]
target_number = 0
result_count = 0    # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    #탈출조건
    if current_index == len(array): #array의 마지막 인덱스라면
        if current_sum == target:
            global result_count  #이미 함수 외부에 result_count = 0 으로 설정했기 때문에 전역 변수를 설정해줘야 함
                                #외부에 있는 변수를 내부에서도 쓰겠다!
            result_count += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - array[current_index])

get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result_count)
