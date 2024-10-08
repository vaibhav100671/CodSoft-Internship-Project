import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 8:
        password_result.config(text="Password length should be at least 8 characters", fg="red")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.config(text=f"Generated Password: {password}", fg="green")

def reset_password():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_result.config(text="")

root = tk.Tk()
root.title("Password Generator")
root.geometry("800x500")

label_name = tk.Label(root, font=("Arial", 18), anchor="w", text="Name:")
label_name.pack(fill=tk.X)

entry_name = tk.Entry(root, borderwidth=5, font=("Arial", 16), fg="#4c4c4c")
entry_name.pack(fill=tk.X)

label_email = tk.Label(root, font=("Arial", 18), anchor="w", text="Email:")
label_email.pack(fill=tk.X)

entry_email = tk.Entry(root, borderwidth=5, font=("Arial", 16), fg="#4c4c4c")
entry_email.pack(fill=tk.X)

label_username = tk.Label(root, font=("Arial", 18), anchor="w", text="Username:")
label_username.pack(fill=tk.X)

entry_username = tk.Entry(root, borderwidth=5, font=("Arial", 16), fg="#4c4c4c")
entry_username.pack(fill=tk.X)

label_length = tk.Label(root, font=("Arial", 18), anchor="w", text="Password Length:")
label_length.pack(fill=tk.X)

length_entry = tk.Entry(root, borderwidth=5, font=("Arial", 16), fg="#4c4c4c")
length_entry.pack(fill=tk.X)
tk.Label(root, text="").pack()

generate_button = tk.Button(root, text="Generate Password", background="#7676ff", font=("Arial", 16), command=generate_password)
generate_button.pack(fill=tk.X)

reset_button = tk.Button(root, text="Reset", font=("Arial", 16), background="#ff6262", command=reset_password)
reset_button.pack(fill=tk.X)

password_result = tk.Label(root, text="", font=("Helvetica", 24))
password_result.pack(fill=tk.X)

root.mainloop()
