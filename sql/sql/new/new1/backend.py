import os
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(lecturer_sql, student_sql):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([lecturer_sql, student_sql])
    similarity = cosine_similarity(tfidf_matrix)[0, 1]
    similarity_percentage = similarity * 100
    return similarity_percentage

def grade_student_submissions(lecturer_sql_file, student_file_or_folder, output_file):
    with open(lecturer_sql_file, 'r') as f:
        lecturer_sql = f.read()
    
    if os.path.isdir(student_file_or_folder):
        student_files = [os.path.join(student_file_or_folder, f) for f in os.listdir(student_file_or_folder) if f.endswith(".sql")]
    else:
        student_files = [student_file_or_folder]
    
    results = []
    for student_file in student_files:
        student_name = os.path.splitext(os.path.basename(student_file))[0]
        with open(student_file, 'r') as f:
            student_sql = f.read()
        similarity = calculate_similarity(lecturer_sql, student_sql)
        results.append((student_name, similarity))
    
    mode = 'w' if not os.path.exists(output_file) else 'a'
    with open(output_file, mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        if mode == 'w':
            writer.writerow(['Student Name', 'Similarity Score (%)'])
        writer.writerows(results)

