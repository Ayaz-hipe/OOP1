class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Студент ставит оценку лектору за лекцию"""
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached and
                1 <= grade <= 10):

            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        # Вычисляем среднюю оценку за все курсы
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        """Сравнение студентов по средней оценке"""
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() < other._get_average_grade()

    def _get_average_grade(self):
        """Вспомогательный метод для подсчета средней оценки"""
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        # Вычисляем среднюю оценку за все лекции
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        """Сравнение лекторов по средней оценке"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() < other._get_average_grade()

    def _get_average_grade(self):
        """Вспомогательный метод для подсчета средней оценки"""
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress and
                1 <= grade <= 10):

            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Функции для подсчета средних оценок по курсу
def calculate_average_hw_grade(students, course):
    """Подсчет средней оценки за домашние задания по всем студентам конкретного курса"""
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    return sum(grades) / len(grades) if grades else 0


def calculate_average_lecture_grade(lecturers, course):
    """Подсчет средней оценки за лекции всех лекторов конкретного курса"""
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    return sum(grades) / len(grades) if grades else 0


# Демонстрация работы
if __name__ == "__main__":
    # Создаем персонажей
    lecturer1 = Lecturer('Иван', 'Иванов')
    reviewer1 = Reviewer('Пётр', 'Петров')
    student1 = Student('Ольга', 'Алёхина', 'Ж')

    # Назначаем курсы
    student1.courses_in_progress += ['Python', 'Java']
    lecturer1.courses_attached += ['Python', 'C++']
    reviewer1.courses_attached += ['Python', 'C++']

    # Тестируем оценку лекций
    print("Оценка лекций:")
    print(student1.rate_lecture(lecturer1, 'Python', 7))  # None (успешно)
    print(student1.rate_lecture(lecturer1, 'Java', 8))  # Ошибка
    print(student1.rate_lecture(lecturer1, 'C++', 8))  # Ошибка
    print(student1.rate_lecture(reviewer1, 'Python', 6))  # Ошибка

    print("\nОценки лектора:")
    print(lecturer1.grades)  # {'Python': [7]}

    # Тестируем оценку домашних работ
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Python', 10)

    print("\nИнформация о персонажах:")
    print("Студент:")
    print(student1)
    print("\nЛектор:")
    print(lecturer1)
    print("\nПроверяющий:")
    print(reviewer1)