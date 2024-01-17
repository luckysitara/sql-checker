#!/usr/bin/python3
import thinter as tk
from tkinter import messagebox
from SQLiteSQLGrader import SQLiteSQLGrader

class SQLiteGraderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite SQL Grader App")

        # Create SQLiteSQLGrader instance
        self.grader = SQLiteSQLGrader('test.db')

        # GUI elements
        self.query_label = tk.Label(root, text="Enter SQL Query:")
        self.query_entry = tk.Entry(root, width=50)
        self.submit_button = tk.Button(root, text="Submit", command=self.evaluate_query)

        # Layout
        self.query_label.grid(row=0, column=0, padx=10, pady=10)
        self.query_entry.grid(row=0, column=1, padx=10, pady=10)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def evaluate_query(self):
        # Get student's SQL query from the entry
        student_query = self.query_entry.get()

        if not student_query:
            messagebox.showerror("Error", "Please enter a SQL query.")
            return

        # Evaluate student's SQL query and get the score
        student_score = self.grader.evaluate_student_sql(student_query)

        # Display the score
        messagebox.showinfo("Score", f"Student's Score: {student_score}")

    def run(self):
        self.root.mainloop()

    def on_exit(self):
        # Close the SQLite connection when exiting the app
        self.grader.close_connection()
        self.root.destroy()

