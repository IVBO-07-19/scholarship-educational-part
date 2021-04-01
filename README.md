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
	
# Launch
	uvicorn main:app --reload
# API Endpoints
List of methods

![image](https://user-images.githubusercontent.com/70891118/112685871-36bc3d00-8e86-11eb-98d6-370bab819475.png)

1. GET get_objects

Request body is empty in this method

URL: http://1365a251a33b.ngrok.io/api/educ_part/example

Answer body example

![image](https://user-images.githubusercontent.com/70891118/112686831-a121ad00-8e87-11eb-8a32-7535b43f8f5b.png)

2. POST put_object

Request body example

![image](https://user-images.githubusercontent.com/70891118/112686401-f0b3a900-8e86-11eb-9647-c1228d06cafe.png)

URL: http://1365a251a33b.ngrok.io/api/educ_part/example

Answer body example

![image](https://user-images.githubusercontent.com/70891118/112686410-f4473000-8e86-11eb-8950-d4ca14593c01.png)

3. GET get_object

Request body is empty in this method

URL: http://1365a251a33b.ngrok.io/api/educ_part/example/{id}

4. PATCH update_object

Request body example

![image](https://user-images.githubusercontent.com/70891118/112687552-b4814800-8e88-11eb-8c91-9bae5f485cb5.png)

URL: http://1365a251a33b.ngrok.io/api/educ_part/example/{id}

Answer body example

![image](https://user-images.githubusercontent.com/70891118/112687605-c531be00-8e88-11eb-9fbf-fff6eb0ce077.png)


5. DELETE delete_object

Request body is empty in this method

URL: http://1365a251a33b.ngrok.io/api/educ_part/example/{id}

Answer body example

![image](https://user-images.githubusercontent.com/70891118/112687704-ea263100-8e88-11eb-85b2-6c02e74aebdf.png)

