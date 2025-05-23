from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
	name: str = "Saurav Kokane"
	age: Optional[int] = None
	email: EmailStr
	cgpa: float = Field(gt=0, lt=10)

new_student = {'email': "sk@gmail.com", 'age':23, 'cgpa': 8.5}

student = Student(**new_student)

print(student)