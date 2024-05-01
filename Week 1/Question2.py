
"""2. A university's Office of Admission keeps
track of student admission application.
Write a simple python code that displays the
information of a student on the
terminal/screen. A student can have a First
name, Surname, Date of Birth, Country, City,
Email, Street Address, College, Programme
of study, Parent name, Parent contact."""



class Student:
    def __init__(self, first_name, last_name, dob, country, city, email, street_address, college, program_of_study, parent_name, parent_contact):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.country = country
        self.city = city
        self.email = email
        self.street_address = street_address
        self.college = college
        self.program_of_study = program_of_study
        self.parent_name = parent_name
        self.parent_contact = parent_contact

    def display_info(self):
        print("Student Information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Date of Birth:", self.dob)
        print("Country:", self.country)
        print("City:", self.city)
        print("Email:", self.email)
        print("Street Address:", self.street_address)
        print("College:", self.college)
        print("Program of Study:", self.program_of_study)
        print("Parent Name:", self.parent_name)
        print("Parent Contact:", self.parent_contact)



student1 = Student("John", "Doe", "2000-01-01", "USA", "New York",
                   "john.doe@example.com", "123 Main St",
                   "University of XYZ", "Computer Science",
                   "Jane Doe", "+1234567890")
student1.display_info()
