
<center><img src="/logo.png" title="로고" alt="올 때 메로나" width="100%"></img></center>




# Pockachip

음성 인식 api를 통해 배달 주문 쉽게 하기(요기요)

## 개발 환경

> python 3.7.2
>
> pipenv 2018.11.26
>
> chromedriver의 경우 window, mac 모두 79.0.3945.36 버전입니다.<br>
>
> 따라서 79버전 이상으로 크롬 업데이트가 필요합니다.

## 사용 모듈(버전)

##### 해당 모듈은 Pipfile.lock에 정리되어 있습니다.

- pyaudio 0.2.11

- selenium 3.141.0

- google 2.0.3

- urllib3 1.25.7

- gcloud 0.18.3

- google-cloud-speech 1.3.1

- pyqt5 5.14.0

- requests 2.22.0

## 가이드 라인

- Google Cloud Platform 가입 및 Google Speech API가 필요합니다.

```

$ git clone https://github.com/juno1028/pokachip.git

$ cd ./pokachip

$ pipenv shell

$ pipenv install

$ python(3) ./pokachip.py

```

## 사용 방법

1. **기본 주소**, **상세 주소**에 주소를 입력합니다.

2. **메뉴 입력** 버튼을 누른 후 아래와 같은 형식으로 원하는 가게와 메뉴, 수량을 말합니다.

   (ex) 맘스터치에서 싸이버거 한개 주문해줘)

   **녹음이 시작되면 빨간색으로 바뀌고 진행되는 동안 유지됩니다.**

3. 녹음이 끝나고 초록색으로 바뀌면 주문한 메뉴를 확인합니다.

4. 만약, 주문하고자 하는 내용과 다르다면 **재입력**을 눌러 다시 녹음합니다.

5. 주문하고자 하는 내용이 맞다면 **주문하기**를 눌러 주문합니다.
