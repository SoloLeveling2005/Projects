import json
import os

import pyaudio
from vosk import Model, KaldiRecognizer
print(os.environ)
BASE_DIR = os.environ['BASE_DIR']
print(BASE_DIR)
model = Model('vosk-model-small-ru-0.4')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen():
    while True:
        data = stream.read(8000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']


for text in listen():
    print(text)
