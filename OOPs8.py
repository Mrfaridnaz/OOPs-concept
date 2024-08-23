class School:

    def __init__(self, class_num, roll_no, name, gender, city, education, parents_name, contact_num, Mathematics, English, Hindi,
                 Chemistry, Physics, grade):

        self.class_num = class_num
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.city = city
        self.education = education
        self.parents_name = parents_name
        self.contact_num = contact_num
        self.Mathematics = Mathematics
        self.English = English
        self.Hindi = Hindi
        self.Chemistry = Chemistry
        self.Physics = Physics
        self.grade = grade

    def address(self):
        return f"Name: {self.name}, City: {self.city}, Parents' Name: {self.parents_name}, Contact Number: {self.contact_num}"

    def calculate_grade(self):
        total_marks = self.Mathematics + self.English + self.Hindi + self.Chemistry + self.Physics
        percentage = (total_marks / 500) * 100
        return f"Total Marks: {total_marks}/500, Percentage: {percentage}%, Grade: {self.grade}"

# Example of creating an instance with correct arguments
farid = School(
    class_num=10,
    roll_no=25,
    name="Farid",
    gender="Male",
    city="Bareilly",
    education="High School",
    parents_name="ABC",
    contact_num="1234567890",
    Mathematics=85,
    English=90,
    Hindi=88,
    Chemistry=92,
    Physics=89,
    grade="A"
)

# Calling the address method
add = farid.address()
print(add)

# Calling the calculate_grade method
grade1 = farid.calculate_grade()
print(grade1)
