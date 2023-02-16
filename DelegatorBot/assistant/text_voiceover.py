import pyttsx3


class Voice:
    def __init__(self):
        pass

    def talk(self, message, lang):
        """
        :param message: Сообщение которое надо озвучить
        :param lang: Язык озвучки. Доступно "ru" - русский и "en" -
        английский
        :return: Озвучка. Возвращает True если озвучка прошла успешно; False(1 параметр), exception_message(2
        параметр) если нет
        """
        try:
            engine = pyttsx3.init()
            engine.setProperty('volume', 3)
            engine.setProperty('rate', 200)

            VOISE_ID = {
                "ru": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0",
                "en": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            }
            # print(VOISE_ID[lang])
            engine.setProperty('voice', VOISE_ID[lang])
            engine.say(message)
            engine.runAndWait()
            return True
        except Exception as e:
            return False, e


