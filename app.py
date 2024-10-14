from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.sampledb2
emps_collection2 = db['emps2']
emp = {"empno": 9001,
       "empname": "Jeff Russell",
       "orders": [2608, 2617, 2620]}
result = emps_collection2.insert_one(emp)
result.inserted_id
emp = emps_collection2.find_one({"empno": 9001})
print(emp)
