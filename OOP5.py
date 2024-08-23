class person:
    def age(self, current_year, year_of_birth):
        return current_year - year_of_birth
    def email_id_input(self, email_id):
        print("take and mail id from a person and print it", email_id)
    def ask_name(self):
        name = input("tell your name")
    def ask_dob(self):
        dob = input("tell your dob")
        return dob
fad = person()
zack = person()
nick = person()
fazz = person()

fad.email_id_input("mrfad83@gmail.com")
fad.ask_name()
fad.ask_dob()