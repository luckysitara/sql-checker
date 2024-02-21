from flask import Flask, render_template, request
from SQLiteSQLGrader import SQLiteSQLGrader

app = Flask(__name__)
grader = SQLiteSQLGrader('test.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    student_query = request.form['student_query']
    score = grader.evaluate_student_sql(student_query)
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
