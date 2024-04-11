import cv2
import numpy as np
import math
from pyzbar.pyzbar import decode
from datetime import datetime 
import time

class QRcode:
    def qr_decode(self,frame):
        # 프레임을 어둡게 만들어서 QR 코드를 더 잘 감지할 수 있도록 함
        dark_frame = cv2.convertScaleAbs(frame, alpha=0.1, beta=0)

        QR = {}

        # 프레임 내에서 QR 코드 디코딩
        decoded_objects = decode(dark_frame)

        for obj in decoded_objects:

            #if obj is not None:
            # QR 코드 데이터 출력
            QR = {"QR" : obj.data.decode('utf-8')}
            #else:
                #QR["QR"] = " "
            # 프레임 내 QR 코드 주위에 사각형 그리기
            cv2.rectangle(frame, (obj.rect.left, obj.rect.top), 
                          (obj.rect.width + obj.rect.left, obj.rect.height + obj.rect.top), 
                          (255, 0, 0), 2)

            return QR

class Shapes:
    def shapes_decode(self,img):


        rec_detected = "" 

        # 이미지를 HSV로 변환
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # 빨간색, 노란색, 초록색, 파란색의 색상 범위 설정
        lower_red = np.array([170, 50, 50])
        upper_red = np.array([180, 255, 255])

        lower_yellow = np.array([15, 50, 50])
        upper_yellow = np.array([30, 255, 255])

        lower_green = np.array([35, 40, 0])
        upper_green = np.array([85, 255, 255])

        lower_blue = np.array([90, 100, 100])
        upper_blue = np.array([130, 255, 255])

        lower_orange = np.array([0,50,50])
        upper_orange = np.array([30,255,255])

        # 각 색상에 대한 마스크 생성
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)

        # 각 마스크를 합치기
        mask =  mask_green | mask_red | mask_yellow | mask_blue | mask_orange

        # 마스크를 이미지에 적용하여 색상을 검출
        masked_image = cv2.bitwise_and(img, img, mask=mask)

        dark_frame = cv2.convertScaleAbs(masked_image, alpha=0.8, beta=2)
        edge_img = cv2.Canny(dark_frame, 100, 200)

        contours, _ = cv2.findContours(edge_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       
        
        for contour in contours:
            approx = cv2.approxPolyDP(contour, cv2.arcLength(contour, True) * 0.02, True)

            if len(approx) == 4 and 23500 < abs(cv2.contourArea(approx)) > 23800: #and cv2.isContourConvex(approx):
                # 사각형의 꼭지점 표시
                for i in range(4):
                    cv2.circle(img, tuple(approx[i][0]), 3, (255, 0, 0), 3)

                for i in range(4):
                    # 사각형의 변 표시
                    cv2.line(img, tuple(approx[i][0]), tuple(approx[(i + 1) % 4][0]), (0, 0, 255), 2)                
                # 이미지 저장
                cv2.imwrite('/home/nsf/사진/rectangle.jpg', img)
                #cnt += 1
                rec_detected = "rectangle"
                break

            

        circles = cv2.HoughCircles(
            edge_img, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=200, param2=25, minRadius=60, maxRadius=90)    
        # 원을 찾았을 경우
        if circles is not None and len(circles) > 0:
            circles = np.round(circles[0, :]).astype("int")
            # 찾은 원들을 이미지에 그리기
            for (x, y, r) in circles:
                cv2.circle(img, (x, y), r, (0, 255, 0), 3)
            # 각 원의 면적을 계산하고, 일정 범위 내에 있는지 확인
            for circle in circles:
                area = np.pi * circle[2] * circle[2]
                print(area)
                if 15000 < area < 18000:
                    rec_detected = "circle"
                    break

        print(rec_detected)

        # 도형 검출 결과를 저장할 딕셔너리 초기화
        shape_result = {}

        # 검출된 도형이 사각형인 경우
        if rec_detected == "rectangle":
            shape_result["Shape"] = "Success"
        # 검출된 도형이 원인 경우
        elif rec_detected == "circle":
            shape_result["Shape"] = "Error"
        # 검출된 도형이 없는 경우
        else:
            shape_result["Shape"] = "Failed"

        return shape_result



# QR코드 및 도형 검출을 위한 QRcode 및 Shapes 객체 생성
qr = QRcode()
shape = Shapes()
       
#웹캠 열기
cap = cv2.VideoCapture(0)
#웹캠 프레임의 너비, 높이 및 FPS 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()
    # 프레임 읽기가 실패한 경우 다음 프레임으로 이동
    if not ret:
        print("캡쳐 오류")
        continue
 
    # QR 코드 검출
    QR = qr.qr_decode(frame)

    # 10회 반복하여 도형 검출 ( 오류 방지를 위한 재시도)
    count = 0
    for count in range(10):
        print(f"count: {count}")
        # 도형 검출 수행
        shape_result = shape.shapes_decode(frame)
        # 도형 검출 결과가 실패가 아닌 경우 반복문 종료
        if shape_result["Shape"] != "Failed":
            break
        count+=1
        # 0.5초 대기
        time.sleep(0.5)
    
    # QR 코드 및 도형 검출 결과 출력
    print(shape_result)
    # QR 코드 및 도형 검출 결과가 모두 있을 경우 병합하여 출력
    if QR is not None and shape_result is not None:
        combined_result = {**QR, **shape_result}
        print(combined_result)
        break
    # 도형 검출 결과가 에러인 경우 빈 QR 코드와 병합하여 출력
    elif shape_result["Shape"] == "Error":
        QR = {"QR": ""}
        combined_result = {**QR, **shape_result}
        print(combined_result)
        break

    # 다음 프레임 읽기
    ret, frame = cap.read()
    # 프레임을 화면에 표시하고 이미지 저장
    cv2.imshow('cam', frame)
    cv2.imwrite(f'/home/nsf/사진/img.jpg', frame)
    cv2.imshow('cam', frame)


