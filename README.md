# Smart_Factory_Project
#### 팀원
강시은: [Github](https://github.com/sieun-20)

백승기: [Github](https://github.com/seunggi-baek)

장유정: [Github](https://github.com/jjang-yu)

김희철

# 프로젝트 설명
객체인식 기술을 활용하여 물체 감지 시스템을 구축하고 해당 물체를 분류하는 서비스.

### 사용 부품

Raspberry pi4 B+, Arduino, LCD, PiCamera V2, WebCam APC480

### 사용 언어

C, C++, Python

### 사용 서비스

Raspberry Pi OS (Legacy, 64-bit), YOLOv5, OpenCV, PyTorch, Arduino IDE, MariaDB, Workbench, Database, Flask

### 분류 항목
1. 이미지 분류(Yolov5)
2. 색상 분류 (Yolov5)
3. 외형 분류(Opencv)
4. QRcode 인식(Opencv)

# 프로젝트 실행

# 프로젝트 설명

### 작동 원리

1) 웹사이트 접속

2) Raspberry Pi(serber) 부팅
   - 부팅 시 Flask 서버 자동 실행

3) 

#### 실제

#### 외부
<img src="https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/e8302163-633d-450a-a181-717406558e0f" width="400" height="300"/>

<img src="https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/4e0582db-38ff-4386-9e0a-c942ce7aba64" width="200" height="300"/>

1-1) 파이캠
1-2) 웹캠
2)  제품 분류 서보모터
3)  컨베이어 스텝모터
4)  적외선 센서
5)  로봇팔 서보모터
6)  제품 카운트 스위치
7)  타워램프
8)  HMI Display

#### 기계실 내부

<img src="https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/9b8e01d2-1204-41c9-aa5e-d68f1db3a99a" width="400" height="300"/>

<img src="https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/8bcb6b7f-eef4-4945-bfee-aee8cc53a714" width="150" height="300"/>

<img src="https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/dd2a24d1-e731-4748-9acf-7bc5fefc9eb4" width="150" height="300"/>

1) 타워램프 외부 전압 12V
2) 컨베이어 스텝모터 드라이버 & 외부 전압 12V
3) 라즈베리파이 (서버)
4) 아두이노 (마스터) & PCB 기판
5) 라즈베리파이 (객체 감지)
6) HMI Display
7) 아두이노 (슬레이브) & 쉴드


#### 객체인식
![객체 인식](https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/888c4f6e-4acb-495d-b9d8-2b20849d4802)

### 회로도
<img src="https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/f1233be5-0b6b-4e00-8388-fda183c82527" width="800" height="600"/>

### PCB 회로도
<img src="https://github.com/jjang-yu/Smart_Factory_Project/assets/160578079/44bd04c6-526e-4c09-9fe1-fbf386b0a033" width="600" height="400"/>
