students = []
flag = 1

def get_students_titlecase():
    students_titlecase = []
    for student in students :
        students_titlecase = student["name"].title()
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):     #sets deault value in function
    student = {"name" : name,  "student_id" : student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not read file")


def read_file():
    try:
        f = open("students.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()

    except Exception:
        print("Could not save file")


read_file()
print_student_titlecase()

while flag:

    student_name = input("Enter student name: ")
    student_id = input("Enter student id: ")
    add_student(student_name, student_id)
    s   = input("Do you want to continue (Y/N): ")
    save_file(student_name)
    if(s == "N" or s == "n"):
        flag = 0

read_file()
print_student_titlecase()




