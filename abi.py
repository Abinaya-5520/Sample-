import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create input field for tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(padx=10, pady=10)

# Create buttons for adding, deleting, and marking tasks as done
add_button = tk.Button(root, text="Add Task")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task")
delete_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done")
done_button.pack(pady=5)

# Create Listbox to display tasks
task_list = tk.Listbox(root, width=50)
task_list.pack(padx=10, pady=10)

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def delete_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete")

def mark_done():
    try:
        task_index = task_list.curselection()[0]
        task = task_list.get(task_index)
        task_list.delete(task_index)
        task_list.insert(task_index, f"[Done] {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done")

def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


    

