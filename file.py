import re
import sqlite3
import requests
import json


print("Waiting... ")
info_about_vac = requests.get(
    "https://api.hh.ru/vacancies?area=4&text=QA+OR+тестировщик&search_field=name"
)
to_python = json.loads(info_about_vac.text)
pages = to_python['pages']
pattern = 'https://api.hh.ru/vacancies/[\d]{8}'
skills = {"Java": 0, "Python": 0, "C#": 0, "Javascript": 0, "Typescript": 0, "Groovy": 0,
          "Ruby": 0, "Php": 0, "Kotlin": 0, "Swift": 0, "Goland": 0, "C\+\+":0
          }
all_text = ""

for i in range(int(pages)):
    url_plus_page = "https://api.hh.ru/vacancies?area=4&text=QA+OR+тестировщик&search_field=name" + \
                    f"&page={i}"
    info_about_vac = requests.get(url_plus_page)
    all_text += info_about_vac.text

search_result = re.findall(pattern, all_text)
filtered_links = set(search_result)


def find_skills():
    for link in filtered_links:
        text_of_link = requests.get(link).text
        changed_text = text_of_link.title()
        for skill in skills:
            if skill == "Javascript" and (re.search("[ ,(]Javascript[\W]", changed_text) 
                                          or re.search("Js[\W]", changed_text)):
                skills[skill] += 1
            elif skill == "Typescript" and (re.search("Typescript[\W]", changed_text) 
                                            or re.search("Ts[\W]", changed_text)):
                skills[skill] += 1
            elif skill == "Goland" and (re.search("Goland[\W]", changed_text) 
                                        or re.search("Go[\W]", changed_text)):
                skills[skill] += 1
            elif skill == "C\+\+" and (re.search("C\+\+[\W]", changed_text)
                                       or re.search("С\+\+[\W]", changed_text)): #russian C
                skills[skill] += 1
            elif re.search(skill + "[\W]", changed_text):
                skills[skill] += 1
            else:
                continue
    return skills

skill = find_skills()


connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()
cur.execute("INSERT INTO skills (all_vacancies, java, python, c_sharp, javascript, typescript, groovy, ruby, php, kotlin, swift, goland, c_plus_plus) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
            (len(filtered_links),
             skill['Java'], 
             skill['Python'], 
             skill['C#'], 
             skill['Javascript'], 
             skill['Typescript'],
             skill['Groovy'], 
             skill['Ruby'], 
             skill['Php'], 
             skill['Kotlin'], 
             skill['Swift'], 
             skill['Goland'],
             skill["C\+\+"]
             )
            )
connection.commit()
connection.close()
