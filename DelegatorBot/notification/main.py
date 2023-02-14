from plyer import notification


def main(title: str = 'Уведомление',
         message: str = 'Delegator запущен',
         timeout: int = 3,
         ticker: str = 'Новое уведомление'):

    notification.notify(
        title=title,
        message=message,
        app_name='Delegator',
        # app_icon='./logo.ico',
        timeout=timeout,
        ticker=ticker,
        toast=True,
        # sound='./sound.wav',
        # urgency='normal',
        # Дополнительные параметры для Windows:
        # выпадающая панель в стиле Windows 10
        # win10_features=True,
        # Цвет фона уведомления
        # app_color=(255, 255, 255),
        # Шрифт текста уведомления
        # font='Arial',
    )
