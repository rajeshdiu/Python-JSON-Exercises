from ast import JoinedStr
import json

python_obj={
    "Name":"Rajesh",
    "Age": 26,
    "Department":"CSE"
}

json_obj=json.dumps(python_obj,sort_keys=True,indent=4)
print(json_obj)


