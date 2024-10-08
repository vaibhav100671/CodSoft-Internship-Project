import tkinter as tk
from tkinter import simpledialog, messagebox
from operator import itemgetter

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Software")

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List Software", font=("Helvetica", 22, "bold"),background=("#fa7919"))
        self.title_label.pack(pady=20)

        self.task_label = tk.Label(root, text="Task Title:", font=("Helvetica", 14, "bold"))
        self.task_label.pack()
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 12), bg="black", fg="white")
        self.task_entry.pack(pady=5)

        self.desc_label = tk.Label(root, text="Description:", font=("Helvetica", 14, "bold"))
        self.desc_label.pack()
        self.desc_entry = tk.Entry(root, width=30, font=("Helvetica", 12), bg="black", fg="white")
        self.desc_entry.pack(pady=5)

        add_button = tk.Button(root, text="Add Task", command=self.add_task, background=("#789af3"))
        add_button.pack(pady=5)

        update_button = tk.Button(root, text="Update Task", command=self.prompt_update_task, background=("#20b35a"))
        update_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.prompt_delete_task, background=("#ec7c74"))
        delete_button.pack(pady=5)

        status_button = tk.Button(root, text="Toggle Status", command=self.prompt_toggle_status, background=("#c5bcf6"))
        status_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        desc = self.desc_entry.get()

        if task:
            self.tasks.append({"Task": task, "Description": desc, "Status": "Pending"})
            self.clear_entries()
            self.show_tasks()
            messagebox.showinfo("Task Added", "Task added successfully!")
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def prompt_update_task(self):
        index = simpledialog.askinteger("Update Task", "Enter the index of the task you want to update:")
        if index is not None and 1 <= index <= len(self.tasks):
            selected_task = self.tasks[index - 1]

            update_window = tk.Toplevel(self.root)
            update_window.title("Update Task")

            task_label = tk.Label(update_window, text="Task Title:")
            task_label.pack()
            task_entry = tk.Entry(update_window, width=30, font=("Helvetica", 12), bg="black", fg="white")
            task_entry.insert(0, selected_task["Task"])
            task_entry.pack(pady=5)

            desc_label = tk.Label(update_window, text="Description:")
            desc_label.pack()
            desc_entry = tk.Entry(update_window, width=30, font=("Helvetica", 12), bg="black", fg="white")
            desc_entry.insert(0, selected_task["Description"])
            desc_entry.pack(pady=5)

            def update_task():
                selected_task["Task"] = task_entry.get()
                selected_task["Description"] = desc_entry.get()
                self.show_tasks()
                update_window.destroy()
                messagebox.showinfo("Task Updated", "Task updated successfully!")

            update_button = tk.Button(update_window, text="Update Task", command=update_task, background="#20b35a")
            update_button.pack(pady=5)
        else:
            messagebox.showwarning("Invalid Index", "Please enter a valid index.")

    
    def prompt_delete_task(self):
        index = simpledialog.askinteger("Delete Task", "Enter the index of the task you want to delete:")
        if index is not None and 1 <= index <= len(self.tasks):
            self.tasks.pop(index - 1)
            self.clear_entries()
            self.show_tasks()
            messagebox.showinfo("Task Deleted", "Task deleted successfully!")
        else:
            messagebox.showwarning("Invalid Index", "Please enter a valid index.")

    def prompt_toggle_status(self):
        index = simpledialog.askinteger("Toggle Status", "Enter the index of the task you want to toggle status:")
        if index is not None and 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task["Status"] = "Completed" if task["Status"] == "Pending" else "Pending"
            self.show_tasks()
        else:
            messagebox.showwarning("Invalid Index", "Please enter a valid index.")
            
    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def show_tasks(self):
        tasks_str = ""
        for idx, task in enumerate(self.tasks, start=1):
            tasks_str += f"{idx}. Task: {task['Task']}\n   Description: {task['Description']}\n   Status: {task['Status']}\n\n"

        if hasattr(self, "tasks_label"):
            self.tasks_label.config(text=tasks_str)
        else:
            self.tasks_label = tk.Label(self.root, text=tasks_str, font=("Helvetica", 12))
            self.tasks_label.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
