class Member:
    def __init__(self, full_name):
        self.full_name = full_name
        
    def greet(self):
        print(f"Hi, my name is {self.full_name}!")

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio= bio
        self.skills =[]
    def add_skill(self, new_skill):
        self.skills.append(new_skill)

class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.student =[]
        self.instructor = []

    def add_participant(self, member):
        if (type(member).__name__) == 'Student':
            self.student.append(member)
        elif (type(member).__name__) == 'Instructor':
            self.instructor.append(member)
        else:
            print("member doesn't exist")
    
    def print_details(self):
        print(f"Workshop details : {self.date}, {self.subject}")
        print("Students:")
        for i, student in enumerate(self.student):
            print(f"{i+1}. {student.full_name} and {student.reason} ")
        print("Instructor:")
        for i, instructor in enumerate(self.instructor):
            print(f"{i+1}. {instructor.full_name} - {instructor.skills}\n and {instructor.bio} ")


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()