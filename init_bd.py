import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO skills (all_vacancies, java, python, c_sharp, javascript, typescript, groovy, ruby, php, kotlin, swift, goland, c_plus_plus) \
            VALUES (200, 66, 56, 21, 22, 2, 7, 2, 2, 12, 6, 6, 1)")

cur.execute("INSERT INTO skills (all_vacancies, java, python, c_sharp, javascript, typescript, groovy, ruby, php, kotlin, swift, goland, c_plus_plus) \
            VALUES (200, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)")


connection.commit()
connection.close()