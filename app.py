import sqlite3
from flask import Flask, render_template


app = Flask(__name__)
skills_of_vacancies = ["Java", "Python", "C#", "JavaScript", "TypeScript", "Groovy", "Ruby", "Php", "Kotlin", "Swift", "Goland", "C++"]

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    skills = conn.execute('SELECT * FROM skills ORDER BY id DESC LIMIT 1').fetchall()
    add_time = skills[0][1]
    all_vacancies = skills[0][2]
    value_of_skills = [skill for skill in skills[0][3:]]

    marge_skills_and_value = dict(zip(skills_of_vacancies, value_of_skills))
    sorted_tuple = sorted(marge_skills_and_value.items(), key=lambda x: x[1], reverse=True)
    sorted_skills = dict(sorted_tuple)
    conn.close()

    return render_template('index.html', skills=sorted_skills, add_time=add_time, all_vacancies=all_vacancies)


app.run(debug=True)