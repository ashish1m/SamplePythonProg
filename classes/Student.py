class Student:

    # class variable
    percent_rise = 5

    def __init__(self, f_name, l_name, age, marks):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.marks = marks
        self.email = f_name + "." + l_name + "@somecompany.com"
        print("Constructor is called")

    def __del__(self):
        print("Destructor is called")

    def full_name(self):
        return "{} {}".format(self.f_name, self.l_name)

    def apply_raise(self):
        self.marks = self.marks * (1 + self.percent_rise / 100)

    def to_string(self):
        return "Name: " + self.f_name + " " + self.l_name + "\n" \
               + "Age: " + str(self.age) + "\n" \
               + "Marks: " + str(self.marks) + "\n" \
               + "Email: " + self.email


std_1 = Student("Ashish", "Mathur", 26, 70)
std_2 = Student("Sunny", "Mathur", 29, 65)

std_1.apply_raise()
print(std_1.to_string())
print(std_2.full_name())
print(std_2.__dict__)
