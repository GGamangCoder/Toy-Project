import random
import sys

running = True

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

sum_player1 = 0
sum_dealer = 0

###### 플레이어 Hit or Stand #######
state_player1 = True
state_dealer = True

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

"""########### 카드 내용 받기 ###########
def change2num():
    with open(".txt", 'r') as file:
        data = file.read()
        Card_list = ['Ace', 'Two', 'Three']     #카드 정보 추가
        
        if data in Card_list:
            return Card_list.index(data)+1
        else:
            #### 생략가능
"""

while running:
    #첫 시작 시 플레이어당 두 장씩 분배
    for i in range(2):
        player1_card.append(giveCard())
        dealer_card.append(giveCard())
    
    ####### 여기서 dealer카드 한 장은 보여지고, 한 장은 가려짐 #######

    ########## check !!!!!!!!!!!!
    sum_player1 = sum(change2num(player1_card))

    print(player1_card, "Player1= {}".format(sum_player1))
    #########플레이어1 카드 뽑기 시작
    while state_player1:    # and state_player2 and state_player3
        if sum_player1 > 21:
            print("Player1: Bust!")
            break
        
        print("Hit = 1 Stand = 2")
        
        choice = int(sys.stdin.readline().rstrip())
        if choice == 1:
            player1_card.append(giveCard())
            sum_player1 = sum(change2num(player1_card))
            print(player1_card, sum_player1)
        elif choice == 2:
            break
        else:
            print("Again!")
    #########플레이어1 카드 뽑기 끝
    
    if sum_player1 <= 21:
        ######### 딜러 합
        sum_dealer = sum(change2num(dealer_card))
        while sum_dealer < 17:
            ######### 카드 추가 될 때마다 사진 추가
            dealer_card.append(giveCard())
            sum_dealer = sum(change2num(dealer_card))
        print(dealer_card, sum_dealer)
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
