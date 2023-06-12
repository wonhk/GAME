import random

def roll_dice():
    min_number = 1
    max_number = 6
    
    random_number = random.randint(min_number, max_number)
    return random_number

def play_game():
    player1 = input("플레이어 1의 이름을 입력하세요: ")
    player2 = input("플레이어 2의 이름을 입력하세요: ")
    
    while True:
        input("Enter를 눌러 주사위를 굴립니다...")
        
        dice1 = roll_dice()
        dice2 = roll_dice()
        
        print(f"{player1}의 주사위: {dice1}")
        print(f"{player2}의 주사위: {dice2}")
        
        if dice1 > dice2:
            print(f"{player1}이(가) 이겼습니다!\n")
        elif dice1 < dice2:
            print(f"{player2}이(가) 이겼습니다!\n")
        else:
            print("비겼습니다! 다시 굴려주세요.\n")
            continue
        
        break

play_game()
