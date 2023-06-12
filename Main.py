import random

sentences = ["확률형 게임에 오신걸 환영합니다", "시작하기전에 간단히 설명 드리겠습니다.",
"게임이 시작되면 랜덤으로 단편 스토리가 등장 할 것입니다", "각 주제 별로 플레이 해야하는 확률형 게임이 등장합니다",
"확률형 게임은 세가지 가위바위보, 주사위, 카드게임이 있습니다", "각 게임에서는 게임 결과에 따라 각각 다른 결과를 맞이하게 될 것 입니다",
"그럼 즐거운 게임 되십시오~"," 스토리는 총 3가지가 존재합니다, 그 중에서 랜덤으로 추첨되면 추첨과 동시에 스토리가 바로 시작됩니다."]

for sentence in sentences:
    print(sentence, end="\n")
    input('>>>')


import story_1

def check_random_number():
    number = random.choice([1, 2, 3])  # 1, 2, 3 중에서 랜덤으로 선택
    if number == 1:
        print('1번 스토리가 선택되었습니다')
        story_1.play_one()
    elif number == 2:
        story_1.play_one()
    else:
        story_1.play_one()

check_random_number()

