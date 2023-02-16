import tkinter as tk


def new_window_message(message_text):
    # Create the main window
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("230x100+100+100")
    root.wm_attributes('-topmost', 1)
    # Create the message
    message = tk.Message(root, text=message_text, font="Arial 11 normal roman", padx=15, pady=15, width=200)
    message.pack(fill='both', expand=True)

    # Set the timer
    root.after(3000, root.destroy)

    # Start the main loop
    root.mainloop()
