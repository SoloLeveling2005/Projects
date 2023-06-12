# import speech_recognition as sr
#
# # Создание объекта Recognizer
# r = sr.Recognizer()
#
# # Запись аудио с микрофона
# with sr.Microphone() as source:
#     print("Говорите что-нибудь...")
#     source.energy_threshold = 200  # ниже значение - выше чувствительность
#     audio = r.listen(source)
#
# # Распознавание речи
# try:
#     text = r.recognize_google(audio, language="ru-RU")
#     print("Вы сказали: " + text)
# except sr.UnknownValueError:
#     print("Не удалось распознать речь")
# except sr.RequestError as e:
#     print("Ошибка сервиса распознавания речи; {0}".format(e))



from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model(r"vosk-model-small-ru-0.22")  # полный путь к модели
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=16000
)
stream.start_stream()

while True:
    data = stream.read(16000)
    if len(data) == 0:
        break
    else:
        print(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult())

print(rec.FinalResult())