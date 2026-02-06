for i in range(1, 32):
    if i % 15 == 0:        # 15의 배수를 가장 먼저 검사
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

