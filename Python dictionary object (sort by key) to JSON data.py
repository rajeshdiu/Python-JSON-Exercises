import json

python_dict={
    "5":4,
    "4":3,
    "1":2,
    "9":8,
    "3":5
}

print("Original String is ",python_dict)
print("\n JSON data:")
print(json.dumps(python_dict, sort_keys=True, indent=4))