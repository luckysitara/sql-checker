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

def upload_lecturer_file():
    filename = filedialog.askopenfilename(title="Select Lecturer's SQL File")
    if filename:
        lecturer_sql_file_entry.delete(0, tk.END)
        lecturer_sql_file_entry.insert(tk.END, filename)

def upload_student_folder():
    foldername = filedialog.askdirectory(title="Select Folder Containing Student Submissions")
    if foldername:
        student_folder_entry.delete(0, tk.END)
        student_folder_entry.insert(tk.END, foldername)

def process_files():
    lecturer_sql_file = lecturer_sql_file_entry.get()
    student_folder = student_folder_entry.get()
    output_file = output_file_entry.get()
    
    # Read lecturer's SQL code
    with open(lecturer_sql_file, 'r') as f:
        lecturer_sql = f.read()
    lecturer_parsed = tokenize_and_parse(lecturer_sql)
    
    # Process student submissions
    results = []
    for filename in os.listdir(student_folder):
        if filename.endswith(".sql"):
            student_name = os.path.splitext(filename)[0]
            student_sql_file = os.path.join(student_folder, filename)
            with open(student_sql_file, 'r') as f:
                student_sql = f.read()
            student_parsed = tokenize_and_parse(student_sql)
            similarity = calculate_similarity(lecturer_parsed, student_parsed)
            results.append((student_name, similarity))
    
    # Save results to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student Name', 'Similarity Score'])
        writer.writerows(results)
    
    print("Grading completed. Results saved to", output_file)

# Create GUI
root = tk.Tk()
root.title("SQL Code Grader")

# Lecturer SQL file
lecturer_sql_frame = tk.Frame(root)
lecturer_sql_frame.pack()
lecturer_sql_label = tk.Label(lecturer_sql_frame, text="Lecturer's SQL File:")
lecturer_sql_label.pack(side=tk.LEFT)
lecturer_sql_file_entry = tk.Entry(lecturer_sql_frame, width=50)
lecturer_sql_file_entry.pack(side=tk.LEFT)
lecturer_sql_upload_button = tk.Button(lecturer_sql_frame, text="Upload", command=upload_lecturer_file)
lecturer_sql_upload_button.pack(side=tk.LEFT)

# Student submissions folder
student_folder_frame = tk.Frame(root)
student_folder_frame.pack()
student_folder_label = tk.Label(student_folder_frame, text="Student Submissions Folder:")
student_folder_label.pack(side=tk.LEFT)
student_folder_entry = tk.Entry(student_folder_frame, width=50)
student_folder_entry.pack(side=tk.LEFT)
student_folder_button = tk.Button(student_folder_frame, text="Upload", command=upload_student_folder)
student_folder_button.pack(side=tk.LEFT)

# Output file
output_file_frame = tk.Frame(root)
output_file_frame.pack()
output_file_label = tk.Label(output_file_frame, text="Output CSV File:")
output_file_label.pack(side=tk.LEFT)
output_file_entry = tk.Entry(output_file_frame, width=50)
output_file_entry.pack(side=tk.LEFT)

# Process button
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack()

root.mainloop()

