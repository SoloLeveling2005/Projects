# Файл: bot.py

import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, ApplicationBuilder
import database
from config import TOKEN


# Функция обработки команды /start
# async def start(update: Update, context) -> None:
#     # Создание кнопки
#     button = KeyboardButton('Нет активных проектов')
#
#     # Создание клавиатуры с одной кнопкой в дополнительном ряду
#     reply_markup = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
#
#     await context.bot.send_message(chat_id=update.effective_chat.id,
#                                    text="Привет! Я бот для управления проектами и задачами.", reply_markup=reply_markup)
#

# Функция обработки команды /start
async def start(update, context):
    projects = database.get_projects()  # Получение списка проектов (здесь предполагается ваша реализация)
    print(projects)
    if len(projects) > 0:
        # Формирование кнопок для существующих проектов
        project_buttons = [KeyboardButton(project[1]) for project in projects]

        # Разделение кнопок на строки по две кнопки
        rows = [project_buttons[i:i + 2] for i in range(0, len(project_buttons), 2)]

        # Добавление кнопки "Проект не выбран"
        rows.append([KeyboardButton(str("Проект не выбран"))])
        print(rows)
        # Создание клавиатуры с кнопками
        reply_markup = ReplyKeyboardMarkup(rows, resize_keyboard=True,
                                           one_time_keyboard=False)

        # Отправка сообщения с клавиатурой
        await update.message.reply_text('Выберите проект:', reply_markup=reply_markup)
    else:
        # Создание клавиатуры с кнопкой "Нет проектов"
        reply_markup = ReplyKeyboardMarkup([[KeyboardButton("Нет проектов")]], resize_keyboard=True,
                                           one_time_keyboard=False)

        # Отправка сообщения с клавиатурой
        await update.message.reply_text('Нет доступных проектов.', reply_markup=reply_markup)


async def button_callback(update, context):
    # Получение текста нажатой кнопки
    button_text = update.message.text

    if button_text == "Проект не выбран":
        # Обработка выбора "Проект не выбран"
        await update.message.reply_text('Вы не выбрали проект.')
    elif button_text == "Нет проектов":
        # Обработка выбора "Нет проектов"
        await update.message.reply_text('Нет доступных проектов.')
    else:
        # Обработка выбора проекта
        await update.message.reply_text(f'Вы выбрали проект: {button_text}')


# Функция обработки команды /addproject
async def add_project(update: Update, context) -> None:
    project_name = ' '.join(context.args)
    project_id = database.create_project(project_name)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Проект '{project_name}' создан. ID проекта: {project_id}")


# Функция обработки команды /deleteproject
async def delete_project(update: Update, context) -> None:
    project_id = int(context.args[0])
    database.delete_project(project_id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Проект с ID {project_id} удален.")


# Функция обработки команды /addtask
async def add_task(update: Update, context) -> None:
    args = context.args
    project_id, title, *description = args
    description = ' '.join(description) if description else ''
    task_id = database.add_task(int(project_id), title, description)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Задача '{title}' добавлена в проект с ID {project_id}. ID задачи: {task_id}")


# Функция обработки команды /updatetask
async def update_task(update: Update, context) -> None:
    args = context.args
    task_id, *task_info = args
    title, description, deadline, status = task_info[:4]
    database.update_task(int(task_id), title, description, deadline, status)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Задача с ID {task_id} обновлена.")


# Функция обработки команды /deletetask
async def delete_task(update: Update, context) -> None:
    task_id = int(context.args[0])
    database.delete_task(task_id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Задача с ID {task_id} удалена.")


# Функция обработки команды /projects
async def list_projects(update: Update, context) -> None:
    projects = database.get_projects()
    if not projects:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Нет доступных проектов.")
    else:
        response = "Список проектов:\n"
        for project in projects:
            response += f"ID: {project[0]}, Name: {project[1]}\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


# Функция обработки неизвестных команд
async def unknown_command(update: Update, context) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Неизвестная команда. Воспользуйтесь доступными командами.")


def main() -> None:
    database.create_projects_table()
    database.create_tasks_table()

    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("addproject", add_project))
    app.add_handler(CommandHandler("deleteproject", delete_project))
    app.add_handler(CommandHandler("addtask", add_task))
    app.add_handler(CommandHandler("updatetask", update_task))
    app.add_handler(CommandHandler("deletetask", delete_task))
    app.add_handler(CommandHandler("projects", list_projects))

    app.run_polling()


if __name__ == '__main__':
    main()
