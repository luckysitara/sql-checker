#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox, filedialog
from SQLiteSQLGrader import SQLiteSQLGrader

class SQLiteGraderApp:
    """
    Tkinter GUI application for SQLite SQL Grader.
    """

    def __init__(self, root):
        """
        Constructor for SQLiteGraderApp.

        Parameters:
        - root: Tkinter root window.
        """
        self.root = root
        self.root.title("SQLite SQL Grader App")

        # Create SQLiteSQLGrader instance
        self.grader = SQLiteSQLGrader('test.db')

        # GUI elements
        self.query_label = tk.Label(root, text="Enter SQL Query:")
        self.query_entry = tk.Entry(root, width=50)
        self.submit_button = tk.Button(root, text="Submit", command=self.evaluate_query)

        self.upload_file_button = tk.Button(root, text="Upload Test Code", command=self.upload_test_code)
        self.upload_file_label = tk.Label(root, text="No file uploaded")

        # Layout
        self.query_label.grid(row=0, column=0, padx=10, pady=10)
        self.query_entry.grid(row=0, column=1, padx=10, pady=10)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.upload_file_button.grid(row=2, column=0, padx=10, pady=10)
        self.upload_file_label.grid(row=2, column=1, padx=10, pady=10)

    def upload_test_code(self):
        """
        Upload test code from a file and populate the entry field.
        """
        file_path = filedialog.askopenfilename(title="Select Test Code File", filetypes=[("SQL Files", "*.sql")])
        if file_path:
            with open(file_path, 'r') as file:
                test_code = file.read()
                self.query_entry.insert(tk.END, test_code)
            self.upload_file_label.config(text=f"File uploaded: {file_path}")

    def evaluate_query(self):
        """
        Evaluate the student's SQL query and display the score.
        """
        # Get student's SQL query from the entry
        student_query = self.query_entry.get()

        if not student_query:
            messagebox.show

