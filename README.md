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
    # Ваш логин
    user = postgres
    # Ваш пароль
    password = postgres
    # Название вашей базы данных
    database = EducationalPart
    # Хост
    host = 127.0.0.1
    # Порт
    port = 5432
````
Для запуска сервиса, надо указать следующую команду:

	uvicorn main:app --reload
# API Endpoints
List of methods

![image](https://user-images.githubusercontent.com/70891118/112685871-36bc3d00-8e86-11eb-98d6-370bab819475.png)

## 1. GET get_objects

Request body is empty in this method

URL: http://1365a251a33b.ngrok.io/api/educ_part/example

Answer body example

```json
[
  [
    1,
    "string1",
    "string1"
  ],
  [
    2,
    "string2",
    "string2"   
  ]
]
```

## 2. POST put_object

Request body example

```json
{
  "field1": "string2",
  "field2": "string2"
}
```

URL: http://1365a251a33b.ngrok.io/api/educ_part/example

Answer body example
```json
[
  [
    1,
    "string1",
    "string1"
  ],
  [
    2,
    "string2",
    "string2"   
  ]
]
```

## 3. GET get_object

Request body is empty in this method

URL: http://1365a251a33b.ngrok.io/api/educ_part/example/{id}

## 4. PATCH update_object

Request body example
```json
{
  "field1": "newstring2",
  "field2": "newstring2"
}
```

URL: http://1365a251a33b.ngrok.io/api/educ_part/example/{id}

Answer body example
```json
[
  [
    2,
    "newstring2",
    "newstring2"
  ]
]
```

## 5. DELETE delete_object

Request body is empty in this method

URL: http://1365a251a33b.ngrok.io/api/educ_part/example/{id}

Answer body example
```json
[
  [
    1,
    "string1",
    "string1"
  ]
]
```

