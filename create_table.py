import configparser

import psycopg2
from psycopg2.extras import RealDictCursor

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')

con = psycopg2.connect(
    database=config.get('postgres', 'database'),
    user=config.get('postgres', 'user'),
    password=config.get('postgres', 'password'),
    host=config.get('postgres', 'host'),
    port=int(config.get('postgres', 'port'))
)

cur = con.cursor(cursor_factory=RealDictCursor)

cur.execute('''create table students
(
    id serial not null,
    id_student int not null,
    full_name varchar not null,
    "group" varchar not null
);
create unique index students_id_student_uindex
    on students (id_student);

create unique index students_id_uindex
    on students (id);

alter table students
    add constraint students_pk
        primary key (id);
''')
cur.execute('''create table excellent_students
(   
    id serial not null,
    id_person int not null
        constraint excellent_students_students_id_person_fk
            references students
                on delete cascade,
    excellent bool default false not null
);
    create unique index excellent_students_id_uindex
        on excellent_students (id);
''')
cur.execute('''create table article_writers
(
    id serial not null,
    id_person int not null
        constraint article_writers_students_id_person_fk
            references students,
    event_name varchar not null,
    prize_place int not null,
    participation varchar not null,
    date date not null,
    scores float default 0 not null
);
    create unique index article_writers_id_uindex
        on article_writers (id);
''')
cur.execute('''create table olympiad_winners
(
    id serial not null,
    id_person int not null
        constraint olympiad_winner_students_id_person_fk
            references students,
    event_name varchar not null,
    level varchar not null,
    prize_place int not null,
    participation varchar not null,
    date date not null,
    scores float default 0 not null
);
    create unique index olympiad_winner_id_uindex
        on olympiad_winner (id);
''')
con.commit()
