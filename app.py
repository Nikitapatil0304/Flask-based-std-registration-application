from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students_data = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    students_data.append((name, email, course))

    return redirect('/students')

@app.route('/students')
def students():
    return render_template('students.html', data=students_data)

if __name__ == "__main__":
    app.run(debug=True)