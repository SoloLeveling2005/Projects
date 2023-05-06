import json
import os
import re
import nltk
import numexpr as ne

import pyaudio
from vosk import Model, KaldiRecognizer
from text_voiceover import Voice
from core import Core
import time


class Assistant(Core):
    def __init__(self, BASE_DIR):
        super().__init__()
        model = Model(f'vosk-model-small-ru-0.4')
        self.data_listen = ""
        self.voice = Voice()
        self.end_time = time.perf_counter()

        self.rec = KaldiRecognizer(model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.stream.start_stream()
        self.go_listen()

    def listen(self):
        while True:
            time_now = time.perf_counter()

            if time_now - self.end_time > 8:
                self.end_time = time_now
                self.data_listen = ""
                print("end")
            else:
                print(time_now - self.end_time)
                data = self.stream.read(10000, exception_on_overflow=False)
                if (self.rec.AcceptWaveform(data)) and (len(data) > 0):
                    answer = json.loads(self.rec.Result())
                    if answer['text']:
                        yield answer['text']

    def go_listen(self):
        for text in self.listen():
            # text = (text.strip()) \
            #     .replace("плюс", "+") \
            #     .replace("минус", "-") \
            #     .replace("один", "1") \
            #     .replace("два", "2") \
            #     .replace("три", "3") \
            #     .replace("четыре", "4") \
            #     .replace("пять", "5") \
            #     .replace("шесть", "6") \
            #     .replace("семь", "7") \
            #     .replace("восемь", "8") \
            #     .replace("девять", "9")
            self.data_listen += text.strip() + " "
            # print(text)
            print(self.data_listen)
            # if self.coincidence(self.data_listen.lower()):
            #     self.data_listen = ""

            # Здесь можно выполнить ваш код

            self.end_time = time.perf_counter()

            # execution_time = end_time - start_time

            # str1 = 'Python'
            # str2 = 'Pthon'
            # ed = nltk.edit_distance(str1, str2)
            # print(ed)


# print(ne.evaluate('3+3+3'))
ass = Assistant("qe")
