import cv2 as cv
import numpy as np
import time
import RPi.GPIO as GPIO
import serial

port = '/dev/ttyACM0'

ser = serial.Serial(port, 9600)

# top left, top right, bottom right, bottom left
def sort_points(points):

    points = points.astype(np.float32)


    new_points = np.zeros((4, 2), dtype = "float32")
 

    s = points.sum(axis = 1)
    min_index = np.argmin(s)
    new_points[0] = points[min_index]
    points = np.delete(points, min_index, axis = 0)


    s = points.sum(axis = 1)
    max_index = np.argmax(s)
    new_points[2] = points[max_index]
    points = np.delete(points, max_index, axis = 0)


    if points[0][1] > points[1][1]:
        new_points[1] = points[1]
        new_points[3] = points[0]
    else:
        new_points[1] = points[0]
        new_points[3] = points[1]
 
    return new_points



def transform(img_input, points):

    points = sort_points(points)
    topLeft, topRight, bottomRight, bottomLeft = points
 
    maxWidth = 400
    maxHeight = 600
 
    
    dst = np.array([[0, 0],[maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],[0, maxHeight - 1]],
        dtype = "float32")
 

    H = cv.getPerspectiveTransform(points, dst)
    img_warped = cv.warpPerspective(img_input, H, (maxWidth, maxHeight))
 
    return img_warped


capture = cv.VideoCapture(0)


cap_num = 100
flag = 1
input = 0
player_turn = 0

while True:

    if flag == 1:
        ret, frame = capture.read(0)
        cv.imshow('Capture', frame)
        
        if ser.read():
            
            print("ok")
            input = int(ser.read())
            print(input)

        if input == 9:
            print("input 9 check")
            ret, frame = capture.read(0)
            cv.imshow('Capture', frame)
            cv.waitKey(1000)
            if not ret:
                break
            cv.imwrite(str(cap_num)+'.jpg', frame)
            input = 0
            flag = 2
        ########## button input()
    
    elif flag == 2:
        print("flag is 2")
        img_color = cv.imread(str(cap_num)+'.jpg', cv.IMREAD_COLOR)
        cap_num += 1

        height,width =img_color.shape[:2]
        #cv.imshow('cap_img', img_color)
        #cv.waitKey(0)


        img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
        #cv.imshow('gray', img_gray)
        #cv.waitKey(0)

        ret, img_binary = cv.threshold(img_gray, 0, 255, 
            cv.THRESH_BINARY|cv.THRESH_OTSU)
        #cv.imshow('binary', img_binary)


        kernel = cv.getStructuringElement( cv.MORPH_RECT, ( 3, 3 ) )
        img_binary = cv.morphologyEx(img_binary, cv.MORPH_OPEN, kernel)
        #cv.imshow('binary_process', img_binary)
        #cv.waitKey(0)



        #contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        _, contours, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


        for contour in contours:

            area = cv.contourArea(contour)

            if area < 100:
                continue


            epsilon = 0.02 * cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, epsilon, True)

    
            size = len(approx)



            img_result = img_color.copy()
            cv.drawContours(img_result, [approx], -1, (0, 255, 0), 2);
            #cv.imshow('@', img_result)
            #cv.waitKey(0)


            if cv.isContourConvex(approx):
                if size == 4:
                    hull = cv.convexHull(approx)


                    points = []

                    for p in hull:
                        points.append(p[0])
                    points = np.array(points)


                    img_card = transform(img_color, points )
                    img_gray = cv.cvtColor(img_card, cv.COLOR_BGR2GRAY)
                    #cv.imshow('transform', img_gray)
                    #cv.waitKey(0)

                    max = -1
                    max_idx = -1

                    '''
                    1~13 spade
                    14~26 clover
                    27~39 heart
                    40~52 diamond
                    '''

                    for i in range(1,53):
                        img_template = cv.imread( str(i) + '.jpg', cv.IMREAD_GRAYSCALE)


                        res = cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF)
                        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

                        if max < max_val:
                            max = max_val
                            max_idx = i

                    img_template = cv.imread( str(max_idx) + '.jpg', cv.IMREAD_GRAYSCALE)
                    img_card = cv.hconcat([img_gray, img_template])

                    cv.imshow('Card', img_card)
                    
                    data = str(max_idx)
                    num = int(data)
                    num = num % 13

                    if num == 0:
                        num = 13
                    
                    data = str(num)
                    
                    with open("CardInfo.txt", "w") as file:
                        file.write(data)

                    time.sleep(2)
                    flag = 3
                    cv.waitKey(2000)
    
    elif flag == 3:
        while True:
            with open("player_turn.txt", "r") as file:
                turn = file.read()
                if turn == '':
                    turn = 0

            player_turn = int(turn)

            if player_turn != 0:
                with open("player_turn.txt", "w") as file:
                    file.write("0")
                    break
        
        ser.write(player_turn)
        flag = 1
