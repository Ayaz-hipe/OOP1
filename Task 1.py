# add class Student
class Student:
    def __init__(self, name, surname, gender):
        # Student attributes: first name, last name, gender
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

def __str__(self):
    return (f"Студент: {self.name} {self.surname}")


# Parent class
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # List of cources taught by a Mentor
        self.courses_attached = []

# Class Lecturer inherits from class Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        #calling the constructor of the parent Mentor class
        super().__init__(name, surname)

    def __str__(self):
        return (f"Лектор: {self.name} {self.surname}")

# class Reviewers inherits from class Mentor
class Reviewer(Mentor):
    def __init__(self, name, surname):
        # calling the constructor of the parent Mentor class
        super().__init__(name, surname)

# method of checking h/w and giving grades to the student
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return (f"Проверявший: {self.name} {self.surname}")


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('John', 'Smith')
cool_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(cool_reviewer)
print(cool_lecturer)