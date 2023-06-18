def play_three():

    sentences = ["진행자 : 자! 서바이벌 프로그램 라스트 게임", "탈락자를 가리기 위한 조커뽑기!",
    "어느덧 마지막 2명만이 남은 상황!", "이 마지막에 뽑는 카드로 게임의 운명이 결정됩니다!","앞전까지 다들 운명의 장난이었는지 조커카드만 골라서 뽑았는데요",
    "이번이 마지막 기회가 될지 기대가 되는 상황입니다.", "나 : 이제 장난은 여기까지 하죠.","슬슬 끝내겠습니다 ㅎㅎ",
    "상대방 : 에이 여태까지 조커 뽑아왔으면서", "이번까지만 뽑아주시죠", "그러고 나서 제가 끝내겠습니다 ㅎㅎ"
    , "진행자 : 양측간의 신경전이 오고가는데요","제 입장에서는 빨리 끝내줬으면 좋겠는데 말이죠","나 : 이번엔 진짜로 끝낸다.."]

    for sentence in sentences:
        print(sentence, end="\n")
        input('>>>')

    num = input ('1. 오른쪽을 뽑는다, 2.왼쪽을 뽑는다. 어느 쪽을 뽑을까? : ')

    if num == '1':
        sentences = ["오른쪽을 뽑았다."]

        for sentence in sentences:
            print(sentence, end="\n")
            input('>>>')
        import Joker
        Joker.play_joker()
    

    
    if num == '2':
        sentences = ["왼쪽을 뽑았다."]

        for sentence in sentences:
            print(sentence, end="\n")
            input('>>>')
        import Joker
        Joker.play_joker()

play_three()
