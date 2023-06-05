import random

def check_random_number():
    number = random.choice([1, 2, 3])  # 1, 2, 3 중에서 랜덤으로 선택
    if number == 1:
        print("첫 번째 숫자가 선택되었습니다.")
    elif number == 2:
        print("두 번째 숫자가 선택되었습니다.")
    else:
        print("세 번째 숫자가 선택되었습니다.")

check_random_number()
