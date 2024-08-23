class Person:
    def __init__(self, name, surname, email_id, year_of_birth):
        self.name = name
        self.surname = surname
        self.email_id = email_id  # This variable will not be used
        self.year_of_birth = year_of_birth

    def age(self, current_year):
        return current_year - self.year_of_birth


farid_var = Person("Farid", "Ansari", "mrfad8392@gmail.com", 1996)

# Using only the 'name', 'surname', and 'year_of_birth' variables
print(farid_var.name + " " + farid_var.surname)
print(farid_var.age(2022))
