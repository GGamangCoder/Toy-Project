import random
import sys

running = True

###### card setting #######
###### pattern = ["♠", "♥", "♣", "♦"]
num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4
card_set = []

for i in num:
    card_set.append(i)

###### user card setting #######
dealer_card = []
player1_card = []
player2_card = []
player3_card = []

sum_player1 = 0
sum_player2 = 0
sum_player3 = 0
sum_dealer = 0

###### 플레이어 Hit or Stand #######
state_player1 = True
state_player2 = True
state_player3 = True
state_dealer = True

def giveCard():
    card = random.choice(card_set)
    card_set.remove(card)
    return card

def change2num(card_list):
    num = []
    for i in card_list:
        if i[0] == 'A':
            num.append(int(1))
        elif i == 'J' or 'Q' or 'K':
            num.append(int(10))
        elif i == '10':
            num.append(int(10))
        else:
            num.append(int(i))
    return num

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

##### 카드 분배
#player1_card.append(giveCard())
#player2_card.append(giveCard())
#player3_card.append(giveCard())
#dealer_card.append(giveCard())


while running:
    #첫 시작 시 플레이어당 두 장씩 분배
    for i in range(2):
        player1_card.append(giveCard())
        player2_card.append(giveCard())
        player3_card.append(giveCard())
        dealer_card.append(giveCard())
    
    ####### 여기서 dealer카드 한 장은 보여지고, 한 장은 가려짐 #######

    ########## check !!!!!!!!!!!!
    sum_player1 = sum(change2num(player1_card))
    sum_player2 = sum(change2num(player2_card))
    sum_player3 = sum(change2num(player3_card))

    print("Player1= {}".format(sum_player1))
    print("Player2= {}".format(sum_player2))
    print("Player3= {}".format(sum_player3))

    #########플레이어1 카드 뽑기 시작
    while state_player1:    # and state_player2 and state_player3
        if sum_player1 > 21:
            print("Player1: Bust!")
            break
        
        print("Player1={}; Go = 1 Stop = 2".format(sum_player1))
        
        choice = int(sys.stdin.readline().rstrip())
        if choice == 1:
            player1_card.append(giveCard())
            sum_player1 = sum(change2num(player1_card))
            print("Player1: ", sum_player1)
        elif choice == 2:
            break
        else:
            print("Again!")
    #########플레이어1 카드 뽑기 끝
    
    #########플레이어2 카드 뽑기 시작
    while state_player2:    # and state_player2 and state_player3
        if sum_player2 > 21:
            print("Player2: Bust!")
            break
        
        print("Player2={}; Go = 1 Stop = 2".format(sum_player2))
        
        choice = int(sys.stdin.readline().rstrip())
        if choice == 1:
            player2_card.append(giveCard())
            sum_player2 = sum(change2num(player2_card))
            print(sum_player2)
        elif choice == 2:
            break
        else:
            print("Again!")
    #########플레이어2 카드 뽑기 끝

    #########플레이어2 카드 뽑기 시작
    while state_player3:    # and state_player2 and state_player3
        if sum_player3 > 21:
            print("Player3: Bust!")
            break
        
        print("Player3={}; Go = 1 Stop = 2".format(sum_player3))
        
        choice = int(sys.stdin.readline().rstrip())
        if choice == 1:
            player3_card.append(giveCard())
            sum_player3 = sum(change2num(player3_card))
            print(sum_player3)
        elif choice == 2:
            break
        else:
            print("Again!")
    #########플레이어3 카드 뽑기 끝

    if sum_player1 <= 21:
        ######### 딜러 합 ###############################
        sum_dealer = sum(change2num(dealer_card))
        while sum_dealer < 17:
            ######### 카드 추가 될 때마다 사진 추가
            dealer_card.append(giveCard())
            sum_dealer = sum(change2num(dealer_card))
        print(sum_dealer)
        ############
        
        if sum_dealer > 21:
            print("Dealer: Bust!")
            print("Player1 win!")
            break
        else:
            if sum_player1 > sum_dealer:
                print("Player1 win!")
                break
            elif sum_player1 == sum_dealer:
                print("Draw")
                break
            else:
                print("Dealer win!")
                break
    else:
        break
