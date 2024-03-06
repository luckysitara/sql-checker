import os
import csv
import sqlparse
import tkinter as tk
from tkinter import filedialog

def tokenize_and_parse(sql_code):
    # Tokenize SQL code
    tokens = sqlparse.parse(sql_code)
    
    # Parse tokens into a structured format (e.g., abstract syntax tree)
    parsed_queries = []
    for token in tokens:
        parsed_queries.append(token.tokens)
    
    return parsed_queries

def calculate_similarity(lecturer_parsed, student_parsed):
    # Compare the structure of parsed SQL queries
    # For simplicity, we'll compare the number of tokens in each query
    lecturer_len = sum(len(query) for query in lecturer_parsed)
    student_len = sum(len(query) for query in student_parsed)
    similarity = min(lecturer_len, student_len) / max(lecturer_len, student_len)
    return similarity

def grade_student_submissions(lecturer_sql_file, student_file_or_folder, output_file):
    # Read lecturer's SQL code
    with open(lecturer_sql_file, 'r') as f:
        lecturer_sql = f.read()
    lecturer_parsed = tokenize_and_parse(lecturer_sql)
    
    # Process student submissions
    if os.path.isdir(student_file_or_folder):
        student_files = [os.path.join(student_file_or_folder, f) for f in os.listdir(student_file_or_folder) if f.endswith(".sql")]
    else:
        student_files = [student_file_or_folder]
    
    results = []
    for student_file in student_files:
        student_name = os.path.splitext(os.path.basename(student_file))[0]
        with open(student_file, 'r') as f:
            student_sql = f.read()
        student_parsed = tokenize_and_parse(student_sql)
        similarity = calculate_similarity(lecturer_parsed, student_parsed)
        results.append((student_name, similarity))
    
    # Save results to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student Name', 'Similarity Score'])
        writer.writerows(results)

def browse_file(entry_widget):
    filename = filedialog.askopenfilename(filetypes=[("SQL files", "*.sql")])
    entry_widget.delete(0, tk.END)
    entry_widget.insert(tk.END, filename)

def browse_folder(entry_widget):
    foldername = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(tk.END, foldername)

def main():
    root = tk.Tk()
    root.title("SQL Grading System")

    lecturer_label = tk.Label(root, text="Lecturer's SQL File:")
    lecturer_label.grid(row=0, column=0, padx=5, pady=5)

    lecturer_entry = tk.Entry(root, width=50)
    lecturer_entry.grid(row=0, column=1, padx=5, pady=5)

    lecturer_button = tk.Button(root, text="Browse", command=lambda: browse_file(lecturer_entry))
    lecturer_button.grid(row=0, column=2, padx=5, pady=5)

    student_label = tk.Label(root, text="Student's SQL File/Folder:")
    student_label.grid(row=1, column=0, padx=5, pady=5)

    student_entry = tk.Entry(root, width=50)
    student_entry.grid(row=1, column=1, padx=5, pady=5)

    student_button = tk.Button(root, text="Browse", command=lambda: browse_file(student_entry))
    student_button.grid(row=1, column=2, padx=5, pady=5)

    student_folder_button = tk.Button(root, text="Browse Folder", command=lambda: browse_folder(student_entry))
    student_folder_button.grid(row=1, column=3, padx=5, pady=5)

    output_label = tk.Label(root, text="Output CSV File:")
    output_label.grid(row=2, column=0, padx=5, pady=5)

    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=2, column=1, padx=5, pady=5)

    def process_files():
        lecturer_sql_file = lecturer_entry.get()
        student_file_or_folder = student_entry.get()
        output_file = output_entry.get()
        grade_student_submissions(lecturer_sql_file, student_file_or_folder, output_file)
        result_label.config(text="Grading completed. Results saved to " + output_file)

    process_button = tk.Button(root, text="Process Files", command=process_files)
    process_button.grid(row=3, column=1, padx=5, pady=5)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

