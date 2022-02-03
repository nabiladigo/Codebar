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
    def add_skill(self, new_skill):
        self.skills.append(new_skill)

class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.student =[]
        self.instructor = []