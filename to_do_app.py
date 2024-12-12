import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root # Instancia de la ventana principal
        self.root.title("Mi lista de tareas") # Título de la ventana
        self.root.geometry("400x600")
        
        # Diseño de la ventana
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Frame principal
        self.main_frame = tk.Frame(self.root, padx=10, pady=10) 
        self.main_frame.grid(sticky="nsew") # Se ajusta al tamaño de la ventana

        self.main_frame.columnconfigure(0, weight=1) 

        # Título
        self.title_label = tk.Label(self.main_frame, text="Mi lista de tareas", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, pady=(10, 20))

        # Entrada de tareas
        self.entry_frame = tk.Frame(self.main_frame)
        self.entry_frame.grid(row=1, column=0, pady=(0, 10), sticky="ew") # Se ajusta al tamaño del frame
        
        self.entry_frame.columnconfigure(0, weight=1) 

        self.task_entry = tk.Entry(self.entry_frame, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, sticky="ew")

        self.add_button = tk.Button(self.entry_frame, text="Agregar", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=(5, 0))

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.main_frame, selectmode=tk.SINGLE, font=("Arial", 12), height=15)
        self.task_listbox.grid(row=2, column=0, sticky="nsew")

        # Botones
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.grid(row=3, column=0, pady=10, sticky="ew")

        self.complete_button = tk.Button(self.buttons_frame, text="Marcar como Completada", command=self.mark_complete)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.buttons_frame, text="Borrar", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Información adicional
        self.info_label = tk.Label(self.main_frame, text="Haz doble click en la tarea para editarla.", font=("Arial", 10), fg="red")
        self.info_label.grid(row=4, column=0, pady=5)

        # Eventos
        self.task_listbox.bind("<Double-Button-1>", self.edit_task)

    def add_task(self): # Método para agregar tareas
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "¡La tarea no puede estar vacía!")

    def delete_task(self): # Método para eliminar tareas
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Advertencia", "¡No hay tarea seleccionada!")

    def mark_complete(self): # Método para marcar tareas como completadas
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            if not task.startswith("[Completada] "):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f"[Completada] {task}")
            else:
                messagebox.showinfo("Info", "¡La tarea ya está completada!")
        else:
            messagebox.showwarning("Advertencia", "¡No hay tarea seleccionada!")

    def edit_task(self, event): # Método para editar tareas
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