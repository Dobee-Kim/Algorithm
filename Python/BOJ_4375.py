"""
문제
2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다.

출력
각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.
"""

# lst = ['1'*(i+1) for i in range(10000)]

# while True:
#     try : 
#         n = int(input()) 

#         # 2와 5로 나눠 떨어지지 않음
#         for i in range(len(lst)):
#             if (int(lst[i])%n==0):
#                 print(i+1)
#                 break

#     except :
#         break


while True:
    try : 
        n = int(input()) 
        number = 1
        digit = 1
        while number%n!=0 :
            number += 10**digit
            digit += 1
        print(digit)        
    except :
        break
