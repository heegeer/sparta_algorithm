def count_down(number):
    #if문은 함수를 빠져나갈 조건
    if number < 0:
        return
    print(number)
    count_down(number - 1)
    #count_down 함수 안에서 count_down을 호출하고 있음


count_down(60)