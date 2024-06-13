from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

user = User(name="John Doe", age=30)






print(user.name)  # prints "John Doe"
print(user.age)   # prints 30

import json
#import datetime
with open("allabolag_2024-06-13 21:56:37.675294.json",'r') as f:
    data = json.loads(f.read())['data']
#print(data)


class KpisValues(BaseModel):
    stringValue: str

class Kpis(BaseModel):
    companyId: int
    countryShortName: str
    marketId: int
    kpisValues: list[KpisValues]

    @field_validator("marketId")
    def check_marketid(cls, v):
        if v <= 0:
            raise ValueError("MarketId cannot be negative")
        return v

for company in data:
    item  = Kpis(**company)
    print(item)
    #print(company["name"])


