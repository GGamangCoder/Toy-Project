###### Setting for random game #######
import sys
import time

###### Setting for pygame #######

import pygame

pygame.init()
running = True

#화면 설정
screen = pygame.display.set_mode((800, 480))
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

#폰트 정의
font = pygame.font.SysFont("msreferencesansserif", 80, True, True)
font_turn = pygame.font.SysFont("msreferencesansserif", 40, True, True)
font_first = pygame.font.SysFont("msreferencesansserif", 60, True, True)

###### 카드 한장 ######
card_set = []   ##################
step = 0        # 버튼 눌리는 경우 Hit or Stand
turn = 0        # player/dealer 순서
num_init = 0    # check deal twice
seq = 0         # player1 to dealer

####### button 눌리는 거
def button(step, turn, running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:              ###### 왜 인식 안되냐
            running = False
        if event.type == pygame.KEYDOWN:
            #print(player1_card, sum(player1_card))
            if event.key == pygame.K_LEFT:         # Hit
                step = 2
            elif event.key == pygame.K_RIGHT:        # Stand
                print("player2:", player2_card, sum(player2_card))
                step = 0
                turn += 1
    return step, turn, running




###### user card setting #######
dealer_card = []
player1_card = []
player2_card = []
player3_card = []

turn_player = 'player'

####### text
text_dealer = font.render(str(sum(dealer_card)), True, WHITE)
text_player1 = font.render(str(sum(player1_card)), True, WHITE)
text_player2 = font.render(str(sum(player2_card)), True, WHITE)
text_player3 = font.render(str(sum(player3_card)), True, WHITE)
text_turn = font_turn.render(str(turn_player), True, WHITE)

######### 카드 분배 함수
def giveCard():
    while True:
        with open("CardInfo.txt", "r") as file:
            data = file.read()
            if data == '':
                data = 0
    
        num = int(data)
        ############# change '10, J, Q, K' to 10
        if num >= 10:
            num = 10

        if num != 0:
            print(num)
            with open("CardInfo.txt", "w") as file:
                file.write("0")
                break

    return num



## 블랙잭 체크
def blackjack(card_list):
    if 1 in card_list:
        if 10  in card_list:
            if sum(card_list) == 11:
                print('blackjack')
                card_list = []
                card_list.append(21)
    return card_list


while running:
    
    #text_dealer = font.render(str(sum(dealer_card)), True, WHITE)
    pos_player1_width = text_player1.get_rect().size[0]/2
    pos_player1_height = text_player1.get_rect().size[1]/2
    pos_player1 = (170-pos_player1_width, 336-pos_player1_height)

    pos_player2_width = text_player2.get_rect().size[0]/2
    pos_player2_height = text_player2.get_rect().size[1]/2
    pos_player2 = (400-pos_player2_width, 336-pos_player2_height)
    
    pos_player3_width = text_player3.get_rect().size[0]/2
    pos_player3_height = text_player3.get_rect().size[1]/2
    pos_player3 = (630-pos_player3_width, 336-pos_player3_height)

    if turn == 0 and num_init == 0:
        if player1_card == []:
            pass
        else:
            text_player1 = font.render(str(player1_card[0]), True, WHITE)
        if player2_card == []:
            pass
        else:
            text_player2 = font.render(str(player2_card[0]), True, WHITE)
        if player3_card == []:
            pass
        else:
            text_player3 = font.render(str(player3_card[0]), True, WHITE)
    else:
        text_player1 = font.render(str(sum(player1_card)), True, WHITE)
        text_player2 = font.render(str(sum(player2_card)), True, WHITE)
        text_player3 = font.render(str(sum(player3_card)), True, WHITE)    

    if turn <= 3:
        text_turn = font_turn.render(turn_player+' '+str(turn), True, WHITE)
        if dealer_card == []:
            pass
        else:
            text_dealer = font_first.render(str(dealer_card[0])+' + X', True, WHITE)
    elif turn == 4:
        text_turn = font_turn.render('dealer', True, WHITE)
        text_dealer = font.render(str(sum(dealer_card)), True, WHITE)

    pos_dealer_width = text_dealer.get_rect().size[0]/2
    pos_dealer_height = text_dealer.get_rect().size[1]/2
    pos_dealer = (400-pos_dealer_width, 138-pos_dealer_height)

    pos_turn = (20, 20)

    ######## 화면 구성 1. 배경 / 2. 플레이어 점수1~3 / 3. 딜러 점수
    screen.blit(Background, (0, 0))
    screen.blit(text_dealer, pos_dealer)
    screen.blit(text_player1, pos_player1)
    screen.blit(text_player2, pos_player2)
    screen.blit(text_player3, pos_player3)
    screen.blit(text_turn, pos_turn)


    pygame.display.flip()

    #초기 상태: 카드 두 장씩 분배
    if turn == 0:
        if num_init == 0:
            if seq == 1:
                player1_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq += 1
            ############# 카드 인식해서 추가 후 로봇팔 움직임
            elif seq == 2:
                player2_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq += 1
            elif seq == 3:
                player3_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq += 1
            elif seq == 4:
                dealer_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq = 1
                num_init += 1

        elif num_init == 1:
            if seq == 1:
                player1_card.append(giveCard())
                player1_card = blackjack(player1_card)
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq += 1
                
            ############# 카드 인식해서 추가 후 로봇팔 움직임
            elif seq == 2:
                player2_card.append(giveCard())
                player2_card = blackjack(player2_card)
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq += 1
            elif seq == 3:
                player3_card.append(giveCard())
                player3_card = blackjack(player3_card)
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq += 1
            elif seq == 4:
                dealer_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(seq))
                seq = 1
                num_init += 1

        elif num_init == 2:
            turn = 1

    elif turn == 1:
        if sum(player1_card) < 21:
            
            if step == 0:       #### 임시
                print("player1:", player1_card, sum(player1_card))
                step = 1
            
            ########### 버튼 눌리는 부분
            elif step == 1:
                step, turn, running = button(step, turn, running)

            elif step == 2:
                player1_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(turn))
                step = 0       #init step
        
        elif sum(player1_card) == 21:
            print("Player1: Blackjack!!")
            turn += 1     # next player

        else:               # 합이 21보다 큰 경우
            print("Player1: Bust!!")
            turn += 1     # next player

    elif turn == 2:
        if sum(player2_card) < 21:

            if step == 0:       #### 임시 
                print("player2:", player2_card, sum(player2_card))
                step = 1

            elif step == 1:
                step, turn, running = button(step, turn, running)

            elif step == 2:
                player2_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(turn))
                step = 0       #init step
        
        elif sum(player2_card) == 21:
            print("Player2: Blackjack!!")
            turn += 1     # next player

        else:               # 합이 21보다 큰 경우
            print("Player2: Bust!!")
            turn += 1     # next player

    elif turn == 3:
        if sum(player3_card) < 21:
            
            if step == 0:       #### 임시
                print("player3:", player3_card, sum(player3_card))
                step = 1

            elif step == 1:
                step, turn, running = button(step, turn, running)

            elif step == 2:
                player3_card.append(giveCard())
                with open("player_turn.txt", "w") as file:
                    file.write(str(turn))
                step = 0       #init step
        
        elif sum(player3_card) == 21:
            print("Player3: Blackjack!!")
            turn += 1     # next player

        else:               # 합이 21보다 큰 경우
            print("Player3: Bust!!")
            turn += 1     # next player

    elif turn == 4:         # dealer
        player_sum = [sum(player1_card), sum(player2_card), sum(player3_card)]
        dealer_card = blackjack(dealer_card)


        if sum(dealer_card) < 17:
            dealer_card.append(giveCard())
            with open("player_turn.txt", "w") as file:
                file.write(str(turn))
            print("Dealer:", dealer_card, sum(dealer_card))
            time.sleep(1)

        else:
            print("end", "Dealer:", dealer_card, sum(dealer_card))
            if sum(dealer_card) > 21:
                print("Dealer: Bust!")
                running = False     # game over
            else:
                for i in player_sum:
                    if i <= 21 :
                        if i > sum(dealer_card):
                            print("Player {}".format(player_sum.index(i)+1), "Win")
                            running = False     # game over
                        elif i == sum(dealer_card):
                            print("Player{}".format(player_sum.index(i)+1), "Draw")
                            running = False     # game over
                        else:
                            print("Player{}".format(player_sum.index(i)+1), "Lose")
                            running = False     # game over
                    elif i > 21 :
                        print("Player{}".format(player_sum.index(i)+1), "Bust")
                        running = False     # game over
                time.sleep(1)

pygame.quit()

######## 21이 넘어서 게임이 이미 끝나버리는 경우
######## print 를 화면 상에 나오게 하기 - bust, lose, win


################"""
