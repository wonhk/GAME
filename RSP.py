import random

def play_rock_paper_scissors(player_choice):
  # 플레이어의 입력을 받습니다.
  # player_choice = input("가위, 바위, 보 중에서 무엇을 낼까요? ")

  # 컴퓨터의 선택을 생성합니다.
  computer_choice = random.choice(['가위', '바위', '보'])

  # 결과를 출력합니다.
  if player_choice == computer_choice:
    print("비겼습니다!")
  elif (player_choice == '가위' and computer_choice == '보') or \
      (player_choice == '바위' and computer_choice == '가위') or \
      (player_choice == '보' and computer_choice == '바위'):
    print("당신이 이겼습니다!")
  else:
    print("컴퓨터가 이겼습니다!")

if __name__ == "__main__":
  play_rock_paper_scissors()



