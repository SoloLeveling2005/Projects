from Сore import Core
import sys

data = [
    {'question': 'Какое количество фруктов и овощей необходимо потреблять в день?',
     'answer': 'Рекомендуется потреблять не менее 400 граммов фруктов и овощей в день.'},
    {'question': 'Какое количество воды необходимо выпивать в день для поддержания здоровья?',
     'answer': 'Рекомендуется выпивать не менее 2 литров воды в день.'},
    {'question': 'Какие продукты помогают укрепить иммунную систему?',
     'answer': 'К ним относятся цитрусовые фрукты, чеснок, имбирь, ягоды, орехи, семена, зеленый чай и т.д.'},
    {'question': 'Какие продукты рекомендуется исключить из рациона для поддержания здоровья?',
     'answer': 'Следует ограничить потребление соли, сахара, жирных и жареных продуктов, фаст-фуда и алкоголя.'}
]

bot = Core()
bot.train(data=data)

# import time
#
# def training_animation():
#     for i in range(10, 101, 10):
#         time.sleep(0.3)
#         progress_bar = "Обучение модели: [{}{}] {}%".format("=" * int(i / 10), " " * (10 - int(i / 10)), i)
#         sys.stdout.write('\r' + progress_bar)
#         sys.stdout.flush()
#
#
# training_animation()
# training_animation()
# training_animation()
# training_animation()
