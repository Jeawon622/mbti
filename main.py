from  MBTI_list import *
from rand_num import *
# print(rand_num_list(5,3))

print("hello")

score_e = 0

score_n = 0

score_f = 0

score_p = 0

score_i = 0

score_s = 0

score_t = 0

score_j = 0

arr_list = rand_num_list(4,3)
#say_hello()

# 적으면 0, 크면 5



for n in arr_list:
    print(MBTI['E'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_e += user_input
    if (user_input > 6):
        user_input = 5
        score_e += user_input
    elif (user_input<0):
        user_input = 0
        score_e += user_input

for n in arr_list:
    print(MBTI['I'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_i += user_input
    if (user_input > 6):
        user_input = 5
        score_i += user_input
    elif (user_input<0):
        user_input = 0
        score_i += user_input   

for n in arr_list:
    print(MBTI['N'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_n += user_input
    if (user_input > 6):
        user_input = 5
        score_n += user_input
    elif (user_input<0):
        user_input = 0
        score_n += user_input

for n in arr_list:
    print(MBTI['S'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_s += user_input
    if (user_input > 6):
        user_input = 5
        score_s += user_input
    elif (user_input<0):
        user_input = 0
        score_s += user_input

for n in arr_list:
    print(MBTI['F'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_f += user_input
    if (user_input > 6):
        user_input = 5
        score_f += user_input
    elif (user_input<0):
        user_input = 0
        score_f += user_input

for n in arr_list:
    print(MBTI['T'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_t += user_input
    if (user_input > 6):
        user_input = 5
        score_t += user_input
    elif (user_input<0):
        user_input = 0
        score_t += user_input


for n in arr_list:
    print(MBTI['P'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_p += user_input
    if (user_input > 6):
        user_input = 5
        score_p += user_input
    elif (user_input<0):
        user_input = 0
        score_p += user_input


for n in arr_list:
    print(MBTI['J'][n])
    user_input = int(input("0~5에서 숫자를 입력하세요"))
    score_j += user_input
    if (user_input > 6):
        user_input = 5
        score_j += user_input
    elif (user_input<0):
        user_input = 0
        score_j += user_input

print(score_i,score_e,score_s,score_n,score_f,score_t,score_p,score_j)