import tkinter as tk
from tkinter import filedialog
from backend import grade_student_submissions

class SQLGradingGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # GUI widgets creation
        self.lecturer_label = tk.Label(self, text="Lecturer's SQL File:")
        self.lecturer_label.grid(row=0, column=0, padx=5, pady=5)

        self.lecturer_entry = tk.Entry(self, width=50)
        self.lecturer_entry.grid(row=0, column=1, padx=5, pady=5)

        self.lecturer_button = tk.Button(self, text="Browse", command=self.browse_lecturer_file)
        self.lecturer_button.grid(row=0, column=2, padx=5, pady=5)

        # Other GUI widgets...
        
    def browse_lecturer_file(self):
        filename = filedialog.askopenfilename(filetypes=[("SQL files", "*.sql")])
        self.lecturer_entry.delete(0, tk.END)
        self.lecturer_entry.insert(tk.END, filename)

    # Other methods...

