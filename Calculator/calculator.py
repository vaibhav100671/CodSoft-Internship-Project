import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=70, borderwidth=5, font=("Courier New", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=40, font=("Helvetica", 12), command=button_equal, background="#08AE54", foreground="white").grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=40, pady=40, font=("Helvetica", 12), command=button_clear, background="#ff6262", foreground="white").grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=40, pady=40, font=("Helvetica", 12), foreground="white", background="#7676ff", command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
