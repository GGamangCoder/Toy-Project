###### Setting for random game #######
import random
import sys

###### Setting for pygame #######

import pygame

pygame.init()
running = True

#화면 설정
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption('Blackjack')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
CYAN  = (  0, 255, 255)
MAGENTA=(255,   0, 255)
YELLOW =(255, 255,   0)

#이미지 불러오기
Background = pygame.image.load("Background.png")
#card1 = pygame.image.load("/card/back.png")

#폰트 정의
font = pygame.font.SysFont("msreferencesansserif", 80, True, True)
font_turn = pygame.font.SysFont("msreferencesansserif", 40, True, True)
font_first = pygame.font.SysFont("msreferencesansserif", 60, True, True)

###### 카드 한장 ######
card_set = []   ##################
step = 0        # 버튼 눌리는 경우 Hit or Stand
turn = 1        # player/dealer 순서

####### button 눌리는 거
def button(step, turn, running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:              ###### 왜 인식 안되냐
            running = False
        if event.type == pygame.KEYDOWN:
            #print(player1_card, sum_player1)
            if event.key == pygame.K_LEFT:         # Hit
                step = 2
            elif event.key == pygame.K_RIGHT:        # Stand
                print("player2:", player2_card, sum_player2)
                step = 0
                turn += 1
    return step, turn, running

######### 카드 관련 함수
def giveCard():
    card = random.choice(card_set)
    card_set.remove(card)
    return card

def change2num(card_list):
    num = []
    for i in card_list:
        if i[0] == "A":
            num.append(int(1))
        elif i[0] in ["J","Q","K"]:
            num.append(int(10))
        elif i[0:2] == "10":
            num.append(int(10))
        else:
            num.append(int(i[0]))
    return num

## 블랙잭 체크
def blackjack(card_list):
    if sum(change2num(card_list)) == 11:
        if change2num(card_list)[0] == 1:
            change2num(card_list)[0] = str(11)
        elif change2num(card_list)[1] == 1:
            change2num(card_list)[1] = str(11)
    return card_list

###### card setting #######
pattern = ["♠", "♥", "♣", "♦"]
num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4
card_set = []
for i in pattern:
    for j in num:
        card_set.append(j+i)

###### user card setting #######
dealer_card = []
player1_card = []
player2_card = []
player3_card = []


#첫 시작 시 플레이어당 두 장씩 분배
for i in range(2):
    player1_card.append(giveCard())
    player2_card.append(giveCard())
    player3_card.append(giveCard())
    dealer_card.append(giveCard())

#### check 블랙잭
player1_card = blackjack(player1_card)
player2_card = blackjack(player2_card)
player3_card = blackjack(player3_card)


######## 플레이어 점수 계산
sum_dealer = sum(change2num(dealer_card))
sum_player1 = sum(change2num(player1_card))
sum_player2 = sum(change2num(player2_card))
sum_player3 = sum(change2num(player3_card))
turn_player = 'player'

####### text
text_dealer = font.render(str(sum_dealer), True, WHITE)
text_player1 = font.render(str(sum_player1), True, WHITE)
text_player2 = font.render(str(sum_player2), True, WHITE)
text_player3 = font.render(str(sum_player3), True, WHITE)
text_turn = font_turn.render(str(turn_player), True, WHITE)

########### 폰트 크기 및 위치 조정 - 가운데
'''
pos_dealer_width = text_dealer.get_rect().size[0]/2
pos_dealer_height = text_dealer.get_rect().size[1]/2
pos_dealer = (640-pos_dealer_width, 230-pos_dealer_height)

pos_player1_width = text_player1.get_rect().size[0]/2
pos_player1_height = text_player1.get_rect().size[1]/2
pos_player1 = (270-pos_player1_width, 560-pos_player1_height)

pos_player2_width = text_player2.get_rect().size[0]/2
pos_player2_height = text_player2.get_rect().size[1]/2
pos_player2 = (640-pos_player2_width, 560-pos_player2_height)

pos_player3_width = text_player3.get_rect().size[0]/2
pos_player3_height = text_player3.get_rect().size[1]/2
pos_player3 = (1010-pos_player3_width, 560-pos_player3_height)
'''


while running:
    #text_dealer = font.render(str(sum_dealer), True, WHITE)
    pos_player1_width = text_player1.get_rect().size[0]/2
    pos_player1_height = text_player1.get_rect().size[1]/2
    pos_player1 = (270-pos_player1_width, 560-pos_player1_height)
    text_player1 = font.render(str(sum_player1), True, WHITE)

    pos_player2_width = text_player2.get_rect().size[0]/2
    pos_player2_height = text_player2.get_rect().size[1]/2
    pos_player2 = (640-pos_player2_width, 560-pos_player2_height)
    text_player2 = font.render(str(sum_player2), True, WHITE)
    
    pos_player3_width = text_player3.get_rect().size[0]/2
    pos_player3_height = text_player3.get_rect().size[1]/2
    pos_player3 = (1010-pos_player3_width, 560-pos_player3_height)
    text_player3 = font.render(str(sum_player3), True, WHITE)
    
    pos_dealer_width = text_dealer.get_rect().size[0]/2
    pos_dealer_height = text_dealer.get_rect().size[1]/2
    pos_dealer = (640-pos_dealer_width, 230-pos_dealer_height)
    #### text_dealer 는 turn제와 같이 마지막 딜러 턴에 공개        
    #text_dealer = font.render(str((dealer_card)[0])+' + X', True, WHITE)
    
    pos_turn = (30, 30)
        
    ######## 화면 구성 1. 배경 / 2. 플레이어 점수1~3 / 3. 딜러 점수
    screen.blit(Background, (0, 0))
    screen.blit(text_dealer, pos_dealer)
    screen.blit(text_player1, pos_player1)
    screen.blit(text_player2, pos_player2)
    screen.blit(text_player3, pos_player3)
    screen.blit(text_turn, pos_turn)
    
    if turn <= 3:
        text_turn = font_turn.render(turn_player+' '+str(turn), True, WHITE)
        text_dealer = font_first.render(str(change2num(dealer_card)[0])+' + X', True, WHITE)
    elif turn == 4:
        text_turn = font_turn.render('dealer', True, WHITE)
        text_dealer = font.render(str(sum_dealer), True, WHITE)

    pygame.display.flip()

    if turn == 1:
        sum_player1 = sum(change2num(player1_card))
        
        if sum_player1 < 21:
            
            if step == 0:       #### 임시
                print("player1:", player1_card, sum_player1)
                step = 1
            
            ########### 버튼 눌리는 부분
            elif step == 1:
                step, turn, running = button(step, turn, running)

            elif step == 2:
                player1_card.append(giveCard())
                step = 0       #init step
        
        elif sum_player1 == 21:
            print("Player1: Blackjack!!")
            turn += 1     # next player

        else:               # 합이 21보다 큰 경우
            print("Player1: Bust!!")
            turn += 1     # next player

    elif turn == 2:
        sum_player2 = sum(change2num(player2_card))
        
        if sum_player2 < 21:

            if step == 0:       #### 임시 
                print("player2:", player2_card, sum_player2)
                step = 1

            elif step == 1:
                step, turn, running = button(step, turn, running)

            elif step == 2:
                player2_card.append(giveCard())
                step = 0       #init step
        
        elif sum_player2 == 21:
            print("Player2: Blackjack!!")
            turn += 1     # next player

        else:               # 합이 21보다 큰 경우
            print("Player2: Bust!!")
            turn += 1     # next player

    elif turn == 3:
        sum_player3 = sum(change2num(player3_card))

        if sum_player3 < 21:
            
            if step == 0:       #### 임시
                print("player3:", player3_card, sum_player3)
                step = 1

            elif step == 1:
                step, turn, running = button(step, turn, running)
                
                """
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        #print(player1_card, sum_player1)
                        if event.key == pygame.K_LEFT:         # Hit
                            step = 2
                        elif event.key == pygame.K_RIGHT:        # Stand
                            print("player3:", player3_card, sum_player3)
                            step = 0
                            turn += 1
                """

            elif step == 2:
                player3_card.append(giveCard())
                step = 0       #init step
        
        elif sum_player3 == 21:
            print("Player3: Blackjack!!")
            turn += 1     # next player

        else:               # 합이 21보다 큰 경우
            print("Player3: Bust!!")
            turn += 1     # next player

    elif turn == 4:         # dealer
        player_sum = [sum_player1, sum_player2, sum_player3]
        
        if sum_dealer < 17:
            dealer_card.append(giveCard())
            sum_dealer = sum(change2num(dealer_card))
            print("Dealer:", dealer_card, sum_dealer)
            pygame.time.wait(1000)

        else:
            print("end", "Dealer:", dealer_card, sum_dealer)
            if sum_dealer > 21:
                print("Dealer: Bust!")
                running = False     # game over
            else:
                for i in player_sum:
                    if i <= 21 :
                        if i > sum_dealer:
                            print("Player {}".format(player_sum.index(i)+1), "Win")
                            running = False     # game over
                        elif i == sum_dealer:
                            print("Player{}".format(player_sum.index(i)+1), "Draw")
                            running = False     # game over
                        else:
                            print("Player{}".format(player_sum.index(i)+1), "Lose")
                            running = False     # game over
                    elif i > 21 :
                        print("Player{}".format(player_sum.index(i)+1), "Bust")
                        running = False     # game over
                pygame.time.wait(1000)

pygame.quit()

################### 시행착오 #######################
# 21이 넘어서 게임이 이미 끝나버리는 경우            #
# A와 10, J, Q, K 가 나오는 경우                   #
# print 를 화면 상에 나오게 하기 - bust, lose, win  #
################################################### 
