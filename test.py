import random
sentences = ["확률형 게임에 오신걸 환영합니다", "시작하기전에 간단히 설명 드리겠습니다.",
"게임이 시작되면 랜덤으로 단편 스토리가 등장 할 것입니다", "각 주제 별로 플레이 해야하는 확률형 게임이 등장합니다",
"확률형 게임은 세가지 가위바위보, 주사위, 카드게임이 있습니다", "각 게임에서는 게임 결과에 따라 각각 다른 결과를 맞이하게 될 것 입니다",
"그럼 즐거운 게임 되십시오~"]

for sentence in sentences:
    print(sentence, end="\n")
    input('>>>')





# 함수들을 요소로 갖는 리스트
topics = [함수들]

# 랜덤하게 함수 선택
random_function = random.choice(topics)

# 선택된 함수 실행
random_function()


