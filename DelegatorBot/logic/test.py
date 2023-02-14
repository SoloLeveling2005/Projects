import tkinter as tk

def get_string_length():
    string = entry.get()
    print("Строка:", string)
    root.destroy()

root = tk.Tk()
root.title("Ввод id телеграмм")
root.geometry("350x150")

# Рассчитаем ширину и высоту экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Рассчитаем центр экрана
x_coord = (screen_width/2) - (350/2)
y_coord = (screen_height/2) - (150/2)

# Установим позицию окна
root.geometry("+%d+%d" % (x_coord, y_coord))


label = tk.Label(root, text="Введите id телеграмм:", font="Arial 11 normal roman")
label.pack(pady=10)

entry = tk.Entry(root, font="Arial 11 normal roman")
entry.pack(pady=10)

button = tk.Button(root, text="OK", command=get_string_length,padx=30, font="Arial 11 normal roman")
button.pack(pady=10)

root.mainloop()