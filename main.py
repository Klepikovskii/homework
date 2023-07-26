# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}

#     def rate_lc(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
#             if course in lecturer.grades:
#                 lecturer.grades[course] += [grade]
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             return 'Ошибка'

#     def __str__(self):
#         average = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
#         res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
#         return res

#     def __lt__(self, other):
#         self.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
#         other.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in other.grades.values()])

#         if not isinstance(other, Student):
#             print('Нет в списке студентов')
#         else:
#             return self.average_grade < other.average_grade             
        
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
        
    
        
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.grades = {}

           

#     def __str__(self):
#         average = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
#         res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}'
#         return res

#     def __lt__(self, other):
#         self.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in self.grades.values()])
#         other.average_grade = sum(sum(self.grades.values(), [])) / sum([len(grade) for grade in other.grades.values()])

#         if not isinstance(other, Student):
#             print('Нет в списке лекторов')
#         else:
#             return self.average_grade < other.average_grade     

    
# class Reviewer(Mentor):
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
        
#     def __str__(self):
#         res = f'Имя: {self.name}\nФамилия: {self.surname}'
#         return res  

# def average_grade_student(list_student, course):
#    res = sum([sum(student.grades[course]) for student in list_student]) / sum([len(student.grades[course]) for student in list_student])
#    print(res)

# def average_grade_lecturer(list_lecturer, course):
#    res = sum([sum(lecturer.grades[course]) for lecturer in list_lecturer]) / sum([len(lecturer.grades[course]) for lecturer in list_lecturer])
#    print(res)              
 
# best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
# best_student_1.courses_in_progress += ['Python']

# best_student_2 = Student('Максим', 'Кирилов', 'your_gender')
# best_student_2.courses_in_progress += ['Python']

# cool_mentor_1 = Reviewer('Евгений', 'Смирнов')
# cool_mentor_1.courses_attached += ['Python']

# cool_mentor_2 = Reviewer('Роман', 'Петров')
# cool_mentor_2.courses_attached += ['Python']

# cool_lecturer_1 = Lecturer('Алексей', 'Алексеев')
# cool_lecturer_1.courses_attached += ['Python']

# cool_lecturer_2 = Lecturer('Сергей', 'Кошкин')
# cool_lecturer_2.courses_attached += ['Python']
 
# cool_mentor_1.rate_hw(best_student_2, 'Python', 10)
# cool_mentor_1.rate_hw(best_student_1, 'Python', 9)
# cool_mentor_1.rate_hw(best_student_1, 'Python', 8)

# cool_mentor_2.rate_hw(best_student_1, 'Python', 9)
# cool_mentor_2.rate_hw(best_student_2, 'Python', 7)
# cool_mentor_2.rate_hw(best_student_2, 'Python', 7)



# best_student_1.rate_lc(cool_lecturer_1, 'Python', 5)
# best_student_1.rate_lc(cool_lecturer_2, 'Python', 7)
# best_student_1.rate_lc(cool_lecturer_1, 'Python', 9)

# best_student_2.rate_lc(cool_lecturer_1, 'Python', 5)
# best_student_2.rate_lc(cool_lecturer_2, 'Python', 7)
# best_student_2.rate_lc(cool_lecturer_1, 'Python', 9)

# # print(best_student_1.grades)
# # print(best_student_2.grades)

# # print(cool_lecturer_1.grades)
# # print(cool_lecturer_2.grades)

# print(cool_mentor_1)
# print() 
# print(cool_lecturer_1)
# print() 
# print(best_student_1)
# print()
# print(cool_mentor_2)
# print() 
# print(cool_lecturer_2)
# print() 
# print(best_student_2)
# print() 
# average_grade_student([best_student_1, best_student_2], 'Python')
# print()
# average_grade_lecturer([cool_lecturer_1, cool_lecturer_2], 'Python')

# Домашняя работа задание №1 (открытие файла)

with open('recipes.txt', 'rt', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        quantity_ing = int(file.readline())
        ingredients_list = []
        for _ in range(quantity_ing):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients_list.append(ingredient)
        file.readline()
        cook_book[dish_name] = ingredients_list
        # print(cook_book) 

# Домашняя работа задание №2 (список продуктов)

    

    def get_shop_list_by_dishes(dishes, person_count):
        shoppinr_list = {}
        for dish, ingr_list in cook_book.items():
            if dish in dishes:
                for ingr in ingr_list:
                    if ingr['ingredient_name'] in shoppinr_list:
                        shoppinr_list[ingr['ingredient_name']]['quantity'] += (int(ingr['quantity']) * person_count)
                    else:                        
                        shoppinr_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': (int(ingr['quantity']) * person_count)}
                       
                       

        # print(shoppinr_list)
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)                
                                  
# Домашняя работа задание №3 (преобразование файлов)

import os

# Путь к папке с файлами
current = os.getcwd()
folder_path = 'folder_task3'

# Список файлов в папке
file_list = ['1.txt', '2.txt', '3.txt']

# Функция для получения количества строк в файле
def get_line_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

# Создаем список кортежей с информацией о файле (имя, количество строк)
file_info = [(file, get_line_count(os.path.join(current, folder_path, file))) for file in file_list]

# Сортируем список по количеству строк
file_info.sort(key=lambda x: x[1])
# Создаем результирующий файл и записываем в него содержимое исходных файлов

with open(os.path.join(current, folder_path, 'result.txt'), 'w', encoding='utf-8') as result_file:
    for file, line_count in file_info:
        result_file.write(f'{file}\n')
        result_file.write(f'{line_count}\n')       
        with open(os.path.join(current, folder_path, file), 'r', encoding='utf-8') as input_file:
            result_file.write(input_file.read())
        result_file.write('\n')
 