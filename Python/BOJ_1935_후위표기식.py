"""
후위 표기식 계산법
예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다. 그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다. 마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

문제
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

출력
계산 결과를 소숫점 둘째 자리까지 출력한다.

예제 입력 1 
5
ABC*+DE/-
1
2
3
4
5
예제 출력 1 
6.20

123*+45/-
num = 123
cal = *
---

예제 입력 2 
1
AA+A+
1
예제 출력 2 
3.00
"""

"""
1. 계산기호만 빼기
2.
"""

import re

#1. 라이브러리X 

cal_list = ['*','+','-','/']
num_list =[]

N = int(input())
expr = int(input())
res = []

def is_numeric(expr):
    expr not in cal_list
    return True

# 개별 문자 순회
for e in expr:
    if is_numeric(e):
        num_list.append(e)
    else :
        


for e in range(len(expr)1,-1)

for n in range(N):
    num_list.append(int(input())
    

#2. 정규표현식 사용    
