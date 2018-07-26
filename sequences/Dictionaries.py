student = {'name': 'Ashish', 'age': 26, 'salary': 30000}

print(student)

# getting a value
print(student['name'])
print(student.get('name'))

# adding or update a key value pair
student['gender'] = 'male'
print(student)

# deleting a key value pair
student.pop('salary')
print(student)
del student['age']
print(student)
