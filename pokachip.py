import pyaudio
import wave
import io
import os
import time
import json
import numpy as np
from playsound import playsound

# selenium.py에서 order 함수 가져옴
from selenum import order
from order import order_data
from ttsEx import synthesize_text


# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# pyqt module
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *


# def openMarona():
#     global form_class
#     form_class = uic.loadUiType("textbrowserTest.ui")[0]

# def save_address():
#     address_dic = dict()
#     address_dic["address1"] = address1
#     address_dic["address2"] = address2

#     with open('./address.json', 'w') as json_files:
#         json.dump(address_dic, json_files)

CHUNK = 1024
RATE = 44100
FORMAT = pyaudio.paInt16
CHANNELS = 1

def Onpyaudio():
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    return p, stream

def measuerVolume(vol):
    data = np.frombuffer(vol, dtype=np.int16)

    n = len(data)
    y = np.fft.fft(data)/n
    y = np.absolute(y)
    y = y[range(int(n/2))]

    return y

def startRecording(p, stream):
    print("Start to record the audio.")

    # FORMAT = pyaudio.paInt16
    # CHANNELS = 1
    
    # 녹음시작
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    return p, stream

def endRecording(p, stream):
    stream.stop_stream()
    stream.close()
    p.terminate()

def saveMP3(p, frames2, fileName):

    wf = wave.open(fileName, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames2))
    wf.close()

def loadAudio(file_name):
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    return audio

def configAudio():
    return types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code='ko-KR')

def determineSilence(stream, frames2):
    criterial_time = 0
    end_time = 0

    while(1):
        vol2 = stream.read(CHUNK)
        frames2.append(vol2)

        maxVolume = max(measuerVolume(vol2))

        # 기준값
        thres_value = 1600

        if maxVolume < thres_value:
            if(criterial_time):
                end_time = time.time()
            else:
                criterial_time = time.time()
            if end_time - criterial_time > 1:
                return frames2
        else:
            criterial_time = 0
            end_time = 0

def clearStream(p):
    return p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
def start():

    p, stream = Onpyaudio()

    while(1):

        # data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        # n = len(data)
        # y = np.fft.fft(data)/n
        # y = np.absolute(y)
        # y = y[range(int(n/2))]
        vol = stream.read(CHUNK)
        maxVolume = max(measuerVolume(vol))
        #print('큰소리 나는지 보는중')

        if maxVolume > 5000:

            p, stream = startRecording(p, stream)

            frames2 = determineSilence(stream, [])
            
            endRecording(p, stream)

            saveMP3(p, frames2, "output.mp3")

            client = speech.SpeechClient()

            # The name of the audio file to transcribe
            file_name = os.path.join(os.path.dirname(__file__), './output.mp3')

            # Loads the audio into memory
            audio = loadAudio(file_name)
            # 오디오 파일 정보 입력
            config = configAudio()

            result = client.recognize(config, audio).results
            
            if(len(result)):
                if "메로나" in str(result[0].alternatives[0].transcript):
                    synthesize_text("부르셨나요?")
                    playsound("output2.mp3")
                    return True

            stream = clearStream(p)

if start():
    form_class = uic.loadUiType("textbrowserTest.ui")[0]


def transcriptOut(response):
    for result in response.results:
       #print('Transcript: {}'.format(result.alternatives[0].transcript))
        menu = result.alternatives[0].transcript
        return menu


class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼에 기능을 할당하는 코드
        self.btn_Start.clicked.connect(self.printTextFunction)
        self.btn_Search.clicked.connect(self.startSearchFunction)
        self.btn_reStart.clicked.connect(self.printTextFunction)
        self.input_adrs1.textChanged.connect(self.printAdrs1Function)
        self.input_adrs2.textChanged.connect(self.printAdrs2Function)

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("logo.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
        self.label_head.setPixmap(self.qPixmapFileVar)

    # 기본주소 입력 시 실행되는 함수. address1에 값 저장
    def printAdrs1Function(self):
        global address1
        address1 = self.input_adrs1.text()

        # print(address1)

    # 상세주소 입력 시 실행되는 함수. address2에 값 저장

    def printAdrs2Function(self):
        global address2
        address2 = self.input_adrs2.text()

        # print(address2)

    def printTextFunction(self):

        # save_address()

        self.box_record.setStyleSheet('background-color:#60B99A')

        # 오디오 파일 설정
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        WAVE_OUTPUT_FILENAME = "output.mp3"

        # 녹음시작
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("Start to record the audio.")
        frames = []

        # silence 기준시간 설정
        criterial_time = 0
        end_time = 0

        while(True):
            data = stream.read(CHUNK)
            frames.append(data)
            # print(time.time())

            data2 = np.frombuffer(data, dtype=np.int16)
            n = len(data2)
            measure = np.fft.fft(data2)/n
            measure = np.absolute(measure)
            measure = measure[(range(int(n/2)))]
            measure_value = max(measure)

            # 기준값
            thres_value = 1600

            if measure_value < thres_value:
                if(criterial_time):
                    # print('1번째 조건 criterial', criterial_time)
                    end_time = time.time()
                    # print('1번째 조건 endtime', end_time)
                else:
                    criterial_time = time.time()
                    # print(criterial_time)

                if end_time - criterial_time > 1:
                    # print('종료')
                    break
            else:
                criterial_time = 0
                end_time = 0
                #print('말하는 중이라 시간 reset')

        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        # 녹음 끝

        # 녹음파일 저장 시작
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        # 녹음파일 저장 끝

        client = speech.SpeechClient()

        # The name of the audio file to transcribe
        file_name = os.path.join(os.path.dirname(__file__), './output.mp3')

        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        # 오디오 파일 정보 입력
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='ko-KR')  # 언어 설정

        # Detects speech in the audio file
        response = client.recognize(config, audio)

        # for result in response.results:
        #print('Transcript: {}' .format(result.alternatives[0].transcript))

        global menu
        menu = transcriptOut(response)

        self.textbrow_Test.setPlainText(menu)

    def startSearchFunction(self):
        store, menu_list, number_list = order_data(menu)
        order(menu_list, address1, address2, store, number_list)

        menuk = menu.replace(" ", "")
        menud = menuk.split("주문")[0]
        synthesize_text(menud+"를"+address1+address2+"로 주문하시겠습니까?")
        playsound("output2.mp3")

    # 프로그램 하단 TextLabel 변경하는 함수
    # def changeTextFunction2(self):
    #     # self.Label이름.setText("String")
    #     # Label에 글자를 바꾸는 메서드
    #     self.label_test.setText(menu)


# PyQt
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
