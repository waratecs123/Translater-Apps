import tkinter as tk
from tkinter import messagebox
from tkinter.constants import GROOVE

def convert_ip():
    ip_address = entry.get()
    try:
        # Проверка корректности IP адреса
        parts = ip_address.split(".")
        if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) < 256 for part in parts):
            raise ValueError("Некорректный IP адрес")

        binary_ip = ".".join(format(int(part), '08b') for part in parts)
        no_dots_ip = binary_ip.replace(".", "")

        # Обновление текстовых меток с результатами
        text22.config(text=binary_ip)
        text32.config(text=no_dots_ip)
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


root = tk.Tk()
root.title("ПЕРЕВОД IPV4 В ДВОИЧНЫЙ КОД")
root.iconbitmap("google_2702602.png")
root.geometry("550x700")
root.resizable(False, False)

frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=15, bg="grey")
frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

frame1 = tk.Frame(root, relief=tk.GROOVE, borderwidth=15, bg="grey")
frame1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

text = tk.Label(frame, text="ВВЕДИТЕ IPV4 АДРЕС:", font=("Arial", 20), fg="white", bg="#4E5754", width=70)
text.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=28, font=("Arial", 25))
entry.pack(padx=10, pady=0, ipady=15)

# Кнопка для конвертации
convert_button = tk.Button(frame, text="ПРЕОБРАЗОВАТЬ", font=("Arial", 20), fg= "white", bg= "#4E5754", command=convert_ip, relief= GROOVE, borderwidth=15, width=28)
convert_button.pack(pady=10)

text2 = tk.Label(frame1, text="ДВОИЧНЫЙ КОД:", font=("Arial", 20), fg="white", bg="#4E5754", width=70)
text2.pack(padx=10, pady=10, ipady=22)

text22 = tk.Label(frame1, text="", font=("Arial", 18), fg="white", bg="#A5A5A5", width=70)
text22.pack(padx=10, pady=0, ipady=25)

text3 = tk.Label(frame1, text="БЕЗ ТОЧЕК:", font=("Arial", 20), fg="white", bg="#4E5754", width=70)
text3.pack(padx=10, pady=10, ipady=15)

text32 = tk.Label(frame1, text="", font=("Arial", 18), fg="white", bg="#A5A5A5", width=70)
text32.pack(padx=10, pady=0, ipady=25)

root.mainloop()


