Pockachip
=============

음성 인식 api를 통해 배달 주문 쉽게 하기(요기요)

## 개발 환경

> python 3.7.2

> pipenv 2018.11.26

> chromedriver의 경우 window, mac 모두 79.0.3945.36 버전입니다.
> 따라서 79버전 이상으로 크롬 업데이트가 필요합니다.

## 사용 모듈(버전)

##### 해당 모듈은 Pipfile.lock에 정리되어 있습니다. 

* pyaudio 0.2.11

* selenium 3.141.0

* google 2.0.3

* urllib3 1.25.7

* gcloud 0.18.3

* google-cloud-speech 1.3.1

* pyqt5 5.14.0

* requests 2.22.0

## 가이드 라인

1. git clone https://github.com/juno1028/pokachip.git
2. cd .\pokachip
3. pipenv install
4. pipenv shell
5. python .\selenium.py

## 사용 방법

1. [주소 입력창]에 주소를 입력합니다.

2. [메뉴 입력] 버튼을 누른 후 아래와 같은 형식으로 원하는 가게와 메뉴, 수량을 말합니다
(ex) 맘스터치에서 싸이버거 한개 주문해줘)
* 녹음이 진행되는 동안 초록색이 유지됩니다.

3. 녹음이 끝나고 빨간색으로 바뀌면 주문한 메뉴를 확인합니다.

4. 
