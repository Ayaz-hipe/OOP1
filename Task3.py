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
        # Вычисляем среднюю оценку за все домашние задания
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        courses_in_progress_str = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет курсов'
        finished_courses_str = ', '.join(self.finished_courses) if self.finished_courses else 'Нет курсов'

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        """Сравнение студентов по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_average_grade() >= other._get_average_grade()

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

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        """Сравнение лекторов по средней оценке за лекции"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_average_grade() >= other._get_average_grade()

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
    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ ===\n")

    # Создаем персонажей
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Мария', 'Петрова')

    reviewer1 = Reviewer('Пётр', 'Сидоров')
    reviewer2 = Reviewer('Анна', 'Кузнецова')

    student1 = Student('Ольга', 'Алёхина', 'Ж')
    student2 = Student('Алексей', 'Смирнов', 'М')

    # Назначаем курсы
    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']

    student2.courses_in_progress += ['Python', 'Java']
    student2.finished_courses += ['Основы программирования']

    lecturer1.courses_attached += ['Python', 'Git']
    lecturer2.courses_attached += ['Python', 'Java']

    reviewer1.courses_attached += ['Python', 'Git']
    reviewer2.courses_attached += ['Java', 'C++']

    # Ставим оценки лекторам
    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Python', 8)
    student1.rate_lecture(lecturer1, 'Git', 10)

    student2.rate_lecture(lecturer2, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Python', 9)
    student2.rate_lecture(lecturer2, 'Java', 8)

    # Ставим оценки студентам
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Git', 8)

    reviewer2.rate_hw(student2, 'Python', 7)
    reviewer2.rate_hw(student2, 'Python', 8)
    reviewer2.rate_hw(student2, 'Java', 9)

    # Выводим информацию о персонажах
    print("=== ПРОВЕРЯЮЩИЕ ===")
    print(reviewer1)
    print()
    print(reviewer2)
    print()

    print("=== ЛЕКТОРЫ ===")
    print(lecturer1)
    print()
    print(lecturer2)
    print()

    print("=== СТУДЕНТЫ ===")
    print(student1)
    print()
    print(student2)
    print()

    # Демонстрация сравнения
    print("=== СРАВНЕНИЕ ===")
    print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
    print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")
    print(f"Студент1 == Студент2: {student1 == student2}")
    print(f"Студент1 >= Студент2: {student1 >= student2}")

    # Демонстрация функций подсчета средних оценок по курсу
    print("\n=== СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ ===")
    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]

    python_avg_hw = calculate_average_hw_grade(students_list, 'Python')
    python_avg_lecture = calculate_average_lecture_grade(lecturers_list, 'Python')

    print(f"Средняя оценка за домашние задания по курсу Python: {python_avg_hw:.1f}")
    print(f"Средняя оценка за лекции по курсу Python: {python_avg_lecture:.1f}")