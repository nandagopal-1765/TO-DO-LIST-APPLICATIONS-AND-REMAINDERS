import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")
def add_task():
    task = e.get()
    if task.strip() != "":
        l.insert(tk.END, task)
        e.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")
def delete_task():
    try:
        s = l.curselection()[0]
        l.delete(s)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")
def clear_tasks():
    l.delete(0, tk.END)
e = tk.Entry(root, width=30)
e.pack(pady=10)
add = tk.Button(root, text="Add Task", width=15, command=add_task)
add.pack(pady=5)
d = tk.Button(root, text="Delete Task", width=15, command=delete_task)
d.pack(pady=5)
c = tk.Button(root, text="Clear All Tasks", width=15, command=clear_tasks)
c.pack(pady=5)
l = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
l.pack(pady=10)
root.mainloop()
