#Класс Студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """Студент ставит оценку лектору"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def average_grade(self):
        """Средняя оценка за все домашние задания"""
        all_grades = [g for grades in self.grades.values() for g in grades]
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else "нет"
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "нет"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()


# Базовый класс для наставников
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Класс Лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        """Средняя оценка за лекции"""
        all_grades = [g for grades in self.grades.values() for g in grades]
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()


# Класс Проверяющих
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Проверяющий ставит оценку студенту"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


# Функции
def average_student_grade(students, course):
    """Средняя оценка за ДЗ по всем студентам в рамках курса"""
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


def average_lecturer_grade(lecturers, course):
    """Средняя оценка за лекции по всем лекторам в рамках курса"""
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


# Полевые испытания
# Студенты
student1 = Student('Руой', 'Эман', 'мужской')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Аня', 'Иванова', 'женский')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

# Лекторы
lecturer1 = Lecturer('Джон', 'Смит')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Кейт', 'Джонсон')
lecturer2.courses_attached += ['Git', 'Python']

# Проверяющие
reviewer1 = Reviewer('Сэм', 'Бадди')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Анна', 'Каренина')
reviewer2.courses_attached += ['Git']

# Проверяющие оценивают студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student1, 'Git', 9)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 8)

student1.rate_lecturer(lecturer2, 'Git', 7)
student1.rate_lecturer(lecturer2, 'Python', 9)

# Вывод информации
print("=== Студенты ===")
print(student1, "\n")
print(student2, "\n")

print("=== Лекторы ===")
print(lecturer1, "\n")
print(lecturer2, "\n")

print("=== Проверяющие ===")
print(reviewer1, "\n")
print(reviewer2, "\n")

# Функции подсчёта средних
print("Средняя оценка студентов по курсу Python:", average_student_grade([student1, student2], 'Python'))
print("Средняя оценка студентов по курсу Git:", average_student_grade([student1, student2], 'Git'))
print("Средняя оценка лекторов по курсу Python:", average_lecturer_grade([lecturer1, lecturer2], 'Python'))
print("Средняя оценка лекторов по курсу Git:", average_lecturer_grade([lecturer1, lecturer2], 'Git'))
