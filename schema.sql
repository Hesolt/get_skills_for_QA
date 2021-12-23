DROP TABLE IF EXISTS skills;

CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    add_time DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d', 'now', 'localtime')),
    all_vacancies INTEGER NOT NULL,
    java INTEGER NOT NULL,
    python INTEGER NOT NULL,
    c_sharp INTEGER NOT NULL,
    javascript INTEGER NOT NULL,
    typescript INTEGER NOT NULL,
    groovy INTEGER NOT NULL,
    ruby INTEGER NOT NULL,
    php INTEGER NOT NULL,
    kotlin INTEGER NOT NULL,
    swift INTEGER NOT NULL,
    goland INTEGER NOT NULL,
    c_plus_plus INTEGER NOT NULL
);