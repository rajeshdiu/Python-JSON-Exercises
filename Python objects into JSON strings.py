import json

python_dict={
    "Name":"Rajesh",
    "Age": 26,
    "Department":"CSE"
}

python_list=["Red","Green","Blue"]
python_strig="This is my String"


json_dict=json.dumps(python_dict)
json_list=json.dumps(python_list)
json_string=json.dumps(python_strig)

print(json_dict)
print(json_list)
print(json_string)