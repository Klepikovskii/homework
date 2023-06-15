class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        self.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
        other.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in other.grades.values()])

        if not isinstance(other, Student):
            print('Нет в списке студентов')
        else:
            return self.average_grade < other.average_grade             
        
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
        average = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}'
        return res

    def __lt__(self, other):
        self.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
        other.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in other.grades.values()])

        if not isinstance(other, Student):
            print('Нет в списке лекторов')
        else:
            return self.average_grade < other.average_grade     

    
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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res  

def average_grade_student(list_student, course):
   res = sum([sum(student.grades[course]) for student in list_student]) / sum([len(student.grades[course]) for student in list_student])
   print(res)

def average_grade_lecturer(list_lecturer, course):
   res = sum([sum(lecturer.grades[course]) for lecturer in list_lecturer]) / sum([len(lecturer.grades[course]) for lecturer in list_lecturer])
   print(res)              
 
best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']

best_student_2 = Student('Максим', 'Кирилов', 'your_gender')
best_student_2.courses_in_progress += ['Python']

cool_mentor_1 = Reviewer('Евгений', 'Смирнов')
cool_mentor_1.courses_attached += ['Python']

cool_mentor_2 = Reviewer('Роман', 'Петров')
cool_mentor_2.courses_attached += ['Python']

cool_lecturer_1 = Lecturer('Алексей', 'Алексеев')
cool_lecturer_1.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Сергей', 'Кошкин')
cool_lecturer_2.courses_attached += ['Python']
 
cool_mentor_1.rate_hw(best_student_2, 'Python', 10)
cool_mentor_1.rate_hw(best_student_1, 'Python', 9)
cool_mentor_1.rate_hw(best_student_1, 'Python', 8)

cool_mentor_2.rate_hw(best_student_1, 'Python', 9)
cool_mentor_2.rate_hw(best_student_2, 'Python', 7)
cool_mentor_2.rate_hw(best_student_2, 'Python', 7)



best_student_1.rate_lc(cool_lecturer_1, 'Python', 5)
best_student_1.rate_lc(cool_lecturer_2, 'Python', 7)
best_student_1.rate_lc(cool_lecturer_1, 'Python', 9)

best_student_2.rate_lc(cool_lecturer_1, 'Python', 5)
best_student_2.rate_lc(cool_lecturer_2, 'Python', 7)
best_student_2.rate_lc(cool_lecturer_1, 'Python', 9)

# print(best_student_1.grades)
# print(best_student_2.grades)

# print(cool_lecturer_1.grades)
# print(cool_lecturer_2.grades)

print(cool_mentor_1)
print() 
print(cool_lecturer_1)
print() 
print(best_student_1)
print()
print(cool_mentor_2)
print() 
print(cool_lecturer_2)
print() 
print(best_student_2)
print() 
average_grade_student([best_student_1, best_student_2], 'Python')
print()
average_grade_lecturer([cool_lecturer_1, cool_lecturer_2], 'Python')
