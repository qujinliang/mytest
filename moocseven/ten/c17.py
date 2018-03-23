import json

json_str = '{"name":"qjl", "age":20}'

student = json.loads(json_str)
print(student['name'])
print(student['age'])