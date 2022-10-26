import json

# These are commands


class STUDENT:

    def __init__(self):
        self.student_name = None
        self.student_age = None
        self.ADD_STUDENT = '3'
        self.PRINT_LIST = '6'
        self.AVG_AGE = '9'
        self.exit = '0'
        self.keep_going = True
        self.choice = None

    def menu(self):
        print("\n\t STUDENTS LIST \n")
        print("3. Add student.")
        print("6. Print List.")
        print("9. Average of age.")
        print("0. Exit\n")

    def add_student(self):
        print("Adding new student....")
        self.student_name = input("Enter the name of the student: ").capitalize()
        self.student_age = int(input("Enter the age of the student: "))
        if self.student_age == 0:
            print("Enter a valid age.")
        else:
            with open("../students.json", "r+") as db:
                new = {"name": self.student_name, "age": self.student_age}
                stu = json.load(db)
                stu["students"].append(new)
                print(stu)
                db.seek(0)
                json.dump(stu, db, indent=6)

    def print_students(self):
        print("List of Students:")
        with open("../students.json", "r+") as db:
            person = json.load(db)
            for i in person["students"]:
                for k, v in i.items():
                    print(f"{k: <5} : {v}")
                print("")

    def avg_age(self):
        print("Average age of students: ")

        with open("../students.json", "r") as db:
            person = json.load(db)
            age = []

            for i in person["students"]:
                for k, v in i.items():
                    if k == 'age':
                        age.append(int(v))
                        count = len(age)

            print(f" The average age of students is {sum(age)/count}")

    def process_choice(self):
        self.choice = input("Enter the operation number: ")
        match self.choice:
            case self.ADD_STUDENT:
                self.add_student()
            case self.PRINT_LIST:
                self.print_students()
            case self.AVG_AGE:
                self.avg_age()
            case self.exit:
                self.keep_going = False
            case _:
                print("Enter the operation number listed above.")

    def start_application(self):
        while self.keep_going:
            self.menu()
            self.process_choice()
