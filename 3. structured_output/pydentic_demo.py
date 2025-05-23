from pydantic import BaseModel, EmailStr
from typing import Optional


class Student(BaseModel):
	name: str = "Saurav Kokane"
	age: Optional[int] = None
	email: EmailStr

new_student = {'email': "sk@gmail.com"}

student = Student(**new_student)

print(student)