class Person:
    def __init__(self, name, surname, email_id, year_of_birth):
        self.name = name
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth = year_of_birth

farid_var = Person("Farid", "Ansari", "mrfad8392@gmail.com", 1996)
faraz_var = Person("faraz", "Ansari", "dsfs@gmail.com", 4654)
junaid_var = Person("Farid", "Ansari", "sdfsf@gmail.com", 6566)
print(farid_var.name, farid_var.surname)
print(faraz_var.name)
print(junaid_var.name)
print(type(farid_var))