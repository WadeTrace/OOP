class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент!")
            return
        return self._average_grade() < other._average_grade()

    def __str__(self):
        result = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def _average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не Лектор!")
            return
        return self._average_grade() < other._average_grade()

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                  f'Средняя оценка за лекции: {self._average_grade()}')
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


nice_student = Student("Игорь", "Иванов", "мужской")
nice_student.courses_in_progress += ["Python", "Git"]
nice_student.finished_courses += ["Введение в программирование"]

not_bad_student = Student("Анастасия", "Заводская", "женский")
not_bad_student.courses_in_progress += ["Python"]
not_bad_student.finished_courses += ["Изучение функций"]

nice_lecturer = Lecturer("Александра", "Малышева")
nice_lecturer.courses_attached += ["Python"]

not_nice_lecturer = Lecturer("Никита", "Станиславский")
not_nice_lecturer.courses_attached += ['Python']

nice_reviewer = Reviewer("Стас", "Борецкий")
nice_reviewer.courses_attached += ['Python']

not_nice_reviewer = Reviewer("Дмитрий", "Рукин")
not_nice_reviewer.courses_attached += ['Python']

nice_reviewer.rate_hw(nice_student, "Python", 10)
nice_reviewer.rate_hw(nice_student, "Python", 7)

nice_reviewer.rate_hw(not_bad_student, "Python", 8)
nice_reviewer.rate_hw(not_bad_student, "Python", 4)

nice_student.rate_lec(nice_lecturer, "Python", 9)
not_bad_student.rate_lec(not_nice_lecturer, "Python", 5)

student_list = [nice_student, not_bad_student]
lecturer_list = [nice_lecturer, not_nice_lecturer]

students_grades_list = []


def average_student_grade(student_list, course):
    for student in student_list:
        for key, value in student.grades.items():
            if key is course:
                students_grades_list.extend(value)
    result = sum(students_grades_list) / len(students_grades_list)
    print(f'Средний бал по всем студентам курса {course}: {result}')


lecturer_grades_list = []


def average_lecturer_grade(lecturer_list, course):
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key is course:
                lecturer_grades_list.extend(value)
    result = sum(lecturer_grades_list) / len(lecturer_grades_list)
    print(f'Средний бал по всем лекторам курса {course}: {result}')


average_student_grade(student_list, 'Python')
average_lecturer_grade(lecturer_list, 'Python')

print(nice_lecturer.grades)
print(not_nice_lecturer.grades)
print(nice_student.grades)
print(not_bad_student.grades)
print(nice_student > not_bad_student)
print(nice_lecturer > not_nice_lecturer)
print(nice_student)
print(not_bad_student)
print(nice_lecturer)
print(not_nice_lecturer)
print(nice_reviewer)
print(not_nice_reviewer)
