import json

with open('json_eample.json', 'r', encoding = 'utf8') as f:
    contents = f.read()
    json_data = json.loads(contents)
print(type(json_data))

for employee in json_data['employees']:
    print(employee['lastname'])


#write
import json

dict_data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

with open('data.json', 'w') as f:
    json.dump(dict_data, f)


with open('data.json', 'r') as f:
    contents = f.read()
    json_data = json.loads(contents)

for employee in json_data['employees']:
    print(employee['lastname'])