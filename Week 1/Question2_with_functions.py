
"""2. A university's Office of Admission keeps
track of student admission application.
Write a simple python code that displays the
information of a student on the
terminal/screen. A student can have a First
name, Surname, Date of Birth, Country, City,
Email, Street Address, College, Programme
of study, Parent name, Parent contact. with functions"""


def student_info(first_name, last_name, dob, country, city, email, street_address,
                 college, program_of_study, parent_name, parent_contact):
    print("Student Information:")
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Date of Birth:", dob)
    print("Country:", country)
    print("City:", city)
    print("Email:", email)
    print("Street Address:", street_address)
    print("College:", college)
    print("Program of Study:", program_of_study)
    print("Parent Name:", parent_name)
    print("Parent Contact:", parent_contact)


def main():
    student_info("John", "Doe", "2000-01-01", "USA", "New York",
            "john.doe@example.com", "123 Main St",
            "University of XYZ", "Computer Science",
            "Jane Doe", "+1234567890")

if __name__ == "__main__":
        main()
