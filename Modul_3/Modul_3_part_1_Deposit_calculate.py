import tkinter as tk
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Расчет накоплений")
window.geometry("400x250")

Deposit_label = Label(window, text="Параметры депозита")
Deposit_label.grid(row=1, column=2, pady = 10)

X_label = Label(window, text="Введите размер вклада")
X_label.grid(row=2, column=1, pady = 10)

X_entry = Entry(window, width=10)
X_entry.grid(row=2, column=2)
X_entry.focus()

P_label = Label(window, text="Введите процент по вкладу")
P_label.grid(row=3, column=1, pady = 10)

P_entry = Entry(window, width=10)
P_entry.grid(row=3, column=2)

Y_label = Label(window, text="Введите желаемый размер вклада")
Y_label.grid(row=4, column=1, pady = 10)

Y_entry = Entry(window, width=10)
Y_entry.grid(row=4, column=2)

def clicked():
    global X_entry
    global P_entry
    global Y_entry
    x1 = int(X_entry.get())
    p1 = int(P_entry.get())
    y1 = int(Y_entry.get())
#    window.destroy()
    for i in range(0, 10000):
        if x1 >= y1:
            break
        while x1 < y1:
            x1 = (x1 + x1*p1*0.01)
            i = i + 1
        if x1 >= y1:
                break
    messagebox.showinfo('Результат', f'Необходимая сумма накопится через {i} лет')
        
btn = Button(window, text="Рассчитать", command=clicked)
btn.grid(row=5, column=2)
window.mainloop()