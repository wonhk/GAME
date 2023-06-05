import random

def generate_random_numbers():
    numbers = []
    for _ in range(1):
        number = random.randrange(1,3)  # 1부터 10 사이의 숫자를 랜덤으로 선택
        numbers.append(number)
    return numbers

random_numbers = generate_random_numbers()
print(random_numbers)
