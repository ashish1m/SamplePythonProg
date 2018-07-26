class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def to_string(self):
        return "Name: " + self.name + "\n" \
               + "Age: " + str(self.age) + "\n" \
               + "Salary: " + str(self.salary)


emp = Employee("Ashish Sarala Mathur", 26, 600000)
print(emp.to_string())
