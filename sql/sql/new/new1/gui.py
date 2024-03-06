import os
import tkinter as tk
from tkinter import filedialog
from backend import grade_student_submissions

class SQLGradingGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Lecturer's SQL File
        self.lecturer_label = tk.Label(self, text="Lecturer's SQL File:")
        self.lecturer_label.grid(row=0, column=0, padx=5, pady=5)

        self.lecturer_entry = tk.Entry(self, width=50)
        self.lecturer_entry.grid(row=0, column=1, padx=5, pady=5)

        self.lecturer_button = tk.Button(self, text="Browse", command=self.browse_lecturer_file)
        self.lecturer_button.grid(row=0, column=2, padx=5, pady=5)

        # Student's SQL File/Folder
        self.student_label = tk.Label(self, text="Student's SQL File/Folder:")
        self.student_label.grid(row=1, column=0, padx=5, pady=5)

        self.student_entry = tk.Entry(self, width=50)
        self.student_entry.grid(row=1, column=1, padx=5, pady=5)

        self.student_button = tk.Button(self, text="Browse", command=self.browse_student_file)
        self.student_button.grid(row=1, column=2, padx=5, pady=5)

        self.student_folder_button = tk.Button(self, text="Browse Folder", command=self.browse_student_folder)
        self.student_folder_button.grid(row=1, column=3, padx=5, pady=5)

        # Output CSV File
        self.output_label = tk.Label(self, text="Output CSV File:")
        self.output_label.grid(row=2, column=0, padx=5, pady=5)

        self.output_entry = tk.Entry(self, width=50)
        self.output_entry.grid(row=2, column=1, padx=5, pady=5)

        # Process Files Button
        self.process_button = tk.Button(self, text="Process Files", command=self.process_files)
        self.process_button.grid(row=3, column=1, padx=5, pady=5)

        # Result Label
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def browse_lecturer_file(self):
        filename = filedialog.askopenfilename(filetypes=[("SQL files", "*.sql")])
        self.lecturer_entry.delete(0, tk.END)
        self.lecturer_entry.insert(tk.END, filename)

    def browse_student_file(self):
        filename = filedialog.askopenfilename(filetypes=[("SQL files", "*.sql")])
        self.student_entry.delete(0, tk.END)
        self.student_entry.insert(tk.END, filename)

    def browse_student_folder(self):
        foldername = filedialog.askdirectory()
        self.student_entry.delete(0, tk.END)
        self.student_entry.insert(tk.END, foldername)

    def process_files(self):
        lecturer_sql_file = self.lecturer_entry.get()
        student_file_or_folder = self.student_entry.get()
        output_file = self.output_entry.get()
        grade_student_submissions(lecturer_sql_file, student_file_or_folder, output_file)
        self.result_label.config(text="Grading completed. Results saved to " + output_file)

