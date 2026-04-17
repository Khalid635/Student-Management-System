class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for s in cls.student_list:
            if s.get_id() == student_id:
                return s
        return None


class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False

        StudentDatabase.add_student(self)

    def get_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print("Already enrolled!")
        else:
            self.__is_enrolled = True
            print("Enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Not enrolled yet!")
        else:
            self.__is_enrolled = False
            print("Dropped successfully.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(self.__student_id, self.__name, self.__department, status)


# -------- Sample Students --------
Student(1, "Khalid", "CSE")
Student(2, "Ayesha", "EEE")
Student(3, "Tanvir", "BBA")


# -------- Menu --------
while True:
    print("\n1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        for s in StudentDatabase.student_list:
            s.view_student_info()

    elif choice == '2':
        sid = int(input("Enter ID: "))
        student = StudentDatabase.find_student(sid)

        if student:
            student.enroll_student()
        else:
            print("Student not found!")

    elif choice == '3':
        sid = int(input("Enter ID: "))
        student = StudentDatabase.find_student(sid)

        if student:
            student.drop_student()
        else:
            print("Student not found!")

    elif choice == '4':
        break

    else:
        print("Invalid choice!")