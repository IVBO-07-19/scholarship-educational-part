# Educational part of scolarship project
Hi, this is the part of scolarship project.

Main technologies :
1. Python
2. FastApi
3. PostgreSql
4. FTP

The list will be supplemented...

# Install
	pip install fastapi[all]
	pip install uvicorn
    pip install psycopg2
    
# Launch
Для подключения к базе данных, надо создать файл config.ini
со следующим содержимым:
````editorconfig
    [postgres]
    # Логин
    user = postgres
    # Пароль
    password = postgres
    # Название базы данных
    database = EducationalPart
    # Хост
    host = 127.0.0.1
    # Порт
    port = 5432
````
Для запуска сервиса, надо указать следующую команду:

	uvicorn main:app --reload
# API Endpoints

Add later

## Article Writer

### 1. GET get_all_article_writers

Endpoint: /api/educ_part/article_writers

Request body is empty in this method

Answer body example

```json
[
  {
    "id": 1,
    "id_person": 1,
    "event_name": "Статья",
    "prize_place": 1,
    "participation": "Индивид",
    "date": "2021-04-08",
    "scores": 234.57
  },
  {
    "id": 2,
    "id_person": 2,
    "event_name": "Что-то",
    "prize_place": 76,
    "participation": "Индивид",
    "date": "2021-04-01",
    "scores": 3474575.57
  }
]
```

### 2. POST create_new_article_writer

Endpoint: /api/educ_part/article_writers

Request body example

```json
{
  "id_person": 0,
  "event_name": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-06",
  "scores": 0
}
```

Answer body example
```json
{
  "id": 1,
  "id_person": 0,
  "event_name": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-06",
  "scores": 0
}
```
## Excellent Student
### 1. GET get_all_excellent_students

Endpoint: /api/educ_part/excellent_students

Request body is empty in this method

Answer body example
```json
[
  {
    "id": 1,
    "id_person": 3,
    "is_excellent": true
  },
  {
    "id": 2,
    "id_person": 2,
    "is_excellent": true
  }
]
```

### 2. POST create_new_excellent_student

Endpoint: /api/educ_part/excellent_students

Request body example
```json
{
  "id_person": 1,
  "is_excellent": true
}
```

Answer body example
```json
{
  "id": 1,
  "id_person": 1,
  "is_excellent": true
}
```
## Olympiad Winner

### 1. GET get_all_olympiad_winner

Endpoint: /api/educ_part/olympiad_winners

Request body is empty in this method

Answer body example
```json
[
  {
    "id": 1,
    "id_person": 3,
    "event_name": "Олимпиада",
    "level": "Мировой",
    "prize_place": 1,
    "participation": "Индивид",
    "date": "2021-04-17",
    "scores": 32124.23
  },
  {
    "id": 2,
    "id_person": 2,
    "event_name": "Физтех",
    "level": "Мировой",
    "prize_place": 35,
    "participation": "Индивид",
    "date": "2021-04-01",
    "scores": 1.23
  }
]
```

### 2. POST create_new_olympiad_winner

Endpoint: /api/educ_part/olympiad_winners

Request body example
```json
{
  "id_person": 2,
  "event_name": "Event",
  "level": "first",
  "prize_place": 56,
  "participation": "who",
  "date": "2021-04-06",
  "scores": 105
}
```

Answer body example
```json
{
  "id": 4,
  "id_person": 2,
  "event_name": "Event",
  "level": "first",
  "prize_place": 56,
  "participation": "who",
  "date": "2021-04-06",
  "scores": 105
}
```
