import json


book={}
book ["Rajesh"]={
    "Name":"Rajesh",
    "Age":27,
    "Address":"Dhaka"
}
book ["Dilip"]={
    "Name":"Dilip",
    "Age":25,
    "Address":"ctg"
}
book ["Dip"]={
    "Name":"Dip",
    "Age":20,
    "Address":"sitakund"
}


book=json.dumps(book, sort_keys=True, indent=4)

with open("C:\\Users\\User\\Desktop\\Python-JSON-Exercises\\book.txt","w") as f:
    f.write(book)

s=open("C:\\Users\\User\\Desktop\\Python-JSON-Exercises\\book.txt","r")
book=s.read()
print("My python dict",book)

book=json.loads(book)

print(type(book))

print(book['Dilip'])
