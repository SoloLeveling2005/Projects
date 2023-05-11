# Файл: database.py

import sqlite3


# Функция создания таблицы проектов
def create_projects_table() -> None:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Функция создания таблицы задач
def create_tasks_table() -> None:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS db (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            deadline TEXT,
            status TEXT,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
    ''')
    conn.commit()
    conn.close()


# Функция получения списка проектов
def get_projects() -> list:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    projects = cursor.fetchall()
    conn.close()
    return projects


# Функция создания проекта
def create_project(name: str, description: str = '') -> int:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO projects (name, description) VALUES (?, ?)', (name, description))
    project_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return project_id


# Функция удаления проекта
def delete_project(project_id: int) -> None:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    conn.commit()
    conn.close()


# Функция добавления задачи
def add_task(project_id: int, title: str, description: str = '', deadline: str = '', status: str = ''):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO db (project_id, title, description, deadline, status) VALUES (?, ?, ?, ?, ?)',
                   (project_id, title, description, deadline, status))
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return task_id


# Функция обновления задачи
def update_task(task_id: int, title: str = '', description: str = '', deadline: str = '', status: str = '') -> None:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE db SET 
        title = ?, description = ?, deadline = ?, status = ? 
        WHERE id = ?
    ''', (title, description, deadline, status, task_id))
    conn.commit()
    conn.close()


# Функция удаления задачи
def delete_task(task_id: int) -> None:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM db WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
