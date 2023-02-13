import pyttsx3


def talk(message, lang):
    """
    :param message: Сообщение которое надо озвучить
    :param lang: Язык озвучки. Доступно "ru" - русский и "en" -
    английский
    :return: Озвучка. Возвращает True если озвучка прошла успешно; False(1 параметр), exception_message(2
    параметр) если нет
    """
    try:
        tts = pyttsx3.init()
        newVoiceRate = 195
        tts.setProperty('rate', newVoiceRate)
        VOISE_ID = {
            "ru": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0",
            "en": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        }
        print(VOISE_ID[lang])
        tts.setProperty('voice', VOISE_ID[lang])
        tts.say(message)
        tts.runAndWait()
        return True
    except Exception as e:
        return False, e


e = talk("Привет. Как думаешь? Сколько будет, 1+1", "en")
print(e)