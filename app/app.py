from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    grade = request.form['grade']
    students.append({'name': name, 'grade': grade})
    return render_template('index.html', students=students)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
