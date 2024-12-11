import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x600")
        
        # Responsive design
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.grid(sticky="nsew")
        
        self.main_frame.columnconfigure(0, weight=1)

        # Title label
        self.title_label = tk.Label(self.main_frame, text="To-Do List", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, pady=(10, 20))

        # Task entry frame
        self.entry_frame = tk.Frame(self.main_frame)
        self.entry_frame.grid(row=1, column=0, pady=(0, 10), sticky="ew")
        
        self.entry_frame.columnconfigure(0, weight=1)

        self.task_entry = tk.Entry(self.entry_frame, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, sticky="ew")

        self.add_button = tk.Button(self.entry_frame, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=(5, 0))

        # Task list
        self.task_listbox = tk.Listbox(self.main_frame, selectmode=tk.SINGLE, font=("Helvetica", 12), height=15)
        self.task_listbox.grid(row=2, column=0, sticky="nsew")

        # Buttons frame
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.grid(row=3, column=0, pady=10, sticky="ew")

        self.complete_button = tk.Button(self.buttons_frame, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.buttons_frame, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Info label
        self.info_label = tk.Label(self.main_frame, text="Double-click a task to edit it.", font=("Helvetica", 10), fg="gray")
        self.info_label.grid(row=4, column=0, pady=5)

        # Bind double-click for editing tasks
        self.task_listbox.bind("<Double-Button-1>", self.edit_task)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            if not task.startswith("[Completed] "):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f"[Completed] {task}")
            else:
                messagebox.showinfo("Info", "Task is already completed!")
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def edit_task(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            old_task = self.task_listbox.get(selected_task_index)
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, old_task)
            self.task_listbox.delete(selected_task_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
