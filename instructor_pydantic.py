import instructor
from pydantic import BaseModel, Field

import ollama

#instructor.patch()

class userdetail(BaseModel):
    name: str
    age: int


user : userdetail = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'extract jason is 25 years old',
  },
])

print(user)
#print(user.age)