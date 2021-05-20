# Educational part of scolarship project
Hi, this is the part of scolarship project.

[![Python application](https://github.com/IVBO-07-19/scholarship-educational-part/actions/workflows/tests.yml/badge.svg)](https://github.com/IVBO-07-19/scholarship-educational-part/actions/workflows/tests.yml)

Испоьзуемые технологии:
1. Python
2. FastApi
3. PostgreSql
4. FTP
5. Auth0

Список будет дополняться...

### Запросы
* #### Article Writers
> * id_person - [String] - идентификатор пользователя
> * event_name - [String] - название мероприятия  
> * prize_place - [Integer] - место в мероприятии  
> * participation - [String] - степень участия
> * date - [Date] - дата мероприятия (гггг.мм.дд)
> * scores - [Integer] - Количество очков

URL: https://brigada2.herokuapp.com/api/educ_part/article_writers/

* #### Excellent Students
> * id_person - [String] - идентификатор пользователя
> * excellent - [Boolean] - отличник ли 

URL: https://brigada2.herokuapp.com/api/educ_part/excellent_students/

* #### Olympiad Winners
> * id_person - [String] - идентификатор пользователя
> * event_name - [String] - название мероприятия
> * level - [String] - уровень мероприятия    
> * prize_place - [Integer] - место в мероприятии  
> * participation - [String] - степень участия
> * date - [Date] - дата мероприятия (гггг.мм.дд)
> * scores - [Integer] - Количество очков

URL: https://brigada2.herokuapp.com/api/educ_part/olympiad_winners/

# Установка
Для использования данного сервиса, вам надо выполнить следующую команду:

	pip install -r .\requirements.txt
    
# Запуск
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
Для регистрации нужен токен: jqWYEMUy2VOU18k6IlpYHkrBoLcC5p69

Для запуска сервиса, надо указать следующую команду:

    uvicorn main:app --reload

# API Endpoints

Add later

## Article Writer

Методы для работы с приложениями для получателей награды (приза) в течение 1-ого года, предшествующего назначению повышенной государственной академической
стипендии, за результаты проектной деятельности и (или) опытно-конструкторской работы.

### 1. GET get_all_article_writers

Endpoint: /api/educ_part/article_writers

Request body is empty in this method

Answer body example

```json
[
  {
    "id": 1,
    "id_person": "hdj23JDSJLdas",
    "event_name": "Статья",
    "prize_place": 1,
    "participation": "Индивид",
    "date": "2021-04-08",
    "scores": 234.57
  },
  {
    "id": 2,
    "id_person": "hdj23JDSJLdas",
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
  "id_person": "hdj23JDSJLdas",
  "event_name": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-06",
  "scores": 0
}
```


### 3. GET get_article_writer

Endpoint: /api/educ_part/article_writers/{id}

Request body is empty in this method

Answer body example

```json
{
  "id": 1,
  "id_person": "hdj23JDSJLdas",
  "event_name": "Мероприятие",
  "prize_place": 56,
  "participation": "Индивид",
  "date": "2021-04-06",
  "scores": 34213
}
```

### 4. PUT update_article_writer
Endpoint: /api/educ_part/article_writers/{id}

Request body example

```json
{
  "event_name": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-07",
  "scores": 0
}
```

Answer body example
```json
{
  "id": 1,
  "id_person": "hdj23JDSJLdas",
  "event_name": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-07",
  "scores": 0
}
```

### 5. DELETE delete_article_writer

Endpoint: /api/educ_part/article_writers/{id}

Request body is empty in this method

Answer body example

```json
{
  "id": 1,
  "id_person": "hdj23JDSJLdas",
  "event_name": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-07",
  "scores": 0
}
```

## Excellent Student

Методы для работы с приложениями для тех, кто получал в течение не менее 2-х следующих 
друг за другом промежуточных 
аттестаций, предшествующих назначению
повышенной государственной академической стипендии, только оценок «отлично»

### 1. GET get_all_excellent_students

Endpoint: /api/educ_part/excellent_students

Request body is empty in this method

Answer body example
```json
[
  {
    "id": 1,
    "id_person": "hdj23JDSJLdas",
    "excellent": true
  },
  {
    "id": 2,
    "id_person": "hdj23JDSJLdas",
    "excellent": true
  }
]
```

### 2. POST create_new_excellent_student

Endpoint: /api/educ_part/excellent_students

Request body example
```json
{
  "excellent": true
}
```

Answer body example
```json
{
  "id": 1,
  "id_person": "hdj23JDSJLdas",
  "excellent": true
}
```

### 3. GET get_excellent_student

Endpoint: /api/educ_part/excellent_students/{id}

Request body is empty in this method

Answer body example

```json
{
  "id": 1,
  "id_person": "hdj23JDSJLdas",
  "excellent": true
}
```

### 4. PUT update_excellent_student
Endpoint: /api/educ_part/excellent_students/{id}

Request body example

```json
{
  "excellent": false
}
```

Answer body example
```json
{
  "id": 1,
  "id_person": "hdj23JDSJLdas",
  "excellent": false
}
```

### 5. DELETE delete_excellent_student

Endpoint: /api/educ_part/excellent_students/{id}

Request body is empty in this method

Answer body example

```json
{
  "id": 1,
  "id_person": "hdj23JDSJLdas",
  "excellent": false
}
```

## Olympiad Winner

Методы для работы с приложениями для победителей или призеров международной, всероссийской, ведомственной или региональной олимпиады, конкурса, соревнования,
состязания или иного мероприятия, направленных на выявление учебных достижений студентов, проведенных в течение 1-ого года,
предшествующего назначению повышенной государственной академической:

### 1. GET get_all_olympiad_winner

Endpoint: /api/educ_part/olympiad_winners

Request body is empty in this method

Answer body example
```json
[
  {
    "id": 1,
    "id_person": "hdj23JDSJLdas",
    "event_name": "Олимпиада",
    "level": "Мировой",
    "prize_place": 1,
    "participation": "Индивид",
    "date": "2021-04-17",
    "scores": 32124.23
  },
  {
    "id": 2,
    "id_person": "hdj23JDSJLdas",
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
  "id_person": "hdj23JDSJLdas",
  "event_name": "Event",
  "level": "first",
  "prize_place": 56,
  "participation": "who",
  "date": "2021-04-06",
  "scores": 105
}
```

### 3. GET get_olympiad_winner

Endpoint: /api/educ_part/olympiad_winners/{id}

Request body is empty in this method

Answer body example

```json
{
  "id": 2,
  "id_person": "hdj23JDSJLdas",
  "event_name": "Физтех",
  "level": "Мировой",
  "prize_place": 35,
  "participation": "Индивид",
  "date": "2021-04-01",
  "scores": 1.23
}
```

### 4. PUT update_olympiad_winner
Endpoint: /api/educ_part/olympiad_winners/{id}

Request body example

```json
{
  "event_name": "string",
  "level": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-07",
  "scores": 0
}
```

Answer body example
```json
{
  "id": 2,
  "id_person": "hdj23JDSJLdas",
  "event_name": "string",
  "level": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-07",
  "scores": 0
}
```

### 5. DELETE delete_olympiad_winner

Endpoint: /api/educ_part/olympiad_winners/{id}

Request body is empty in this method

Answer body example

```json
{
  "id": 2,
  "id_person": "hdj23JDSJLdas",
  "event_name": "string",
  "level": "string",
  "prize_place": 0,
  "participation": "string",
  "date": "2021-04-07",
  "scores": 0
}
```
