class Human:
    def __init__(self, name):
        self.name = name


class Teacher(Human):
    def __init__(self, name, subject, schedule):
        super().__init__(name)
        self.name = name
        self.subject = subject
        self.schedule = schedule

    def teacher_is_free(self, day, lesson):
        return self.schedule[day][lesson] == "-"


class Student(Human):
    pass


math_ivanov = Teacher("Ivanov", "Math", [
    ["Math", "Math", "-", "-", "-", "-", "-", "-"],
    ["Math", "-", "-", "Math", "-", "-", "-", "-"],
    ["-", "Math", "Math", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["Math", "-", "-", "Math", "-", "-", "-", "-"]
])

math_kuznetsov = Teacher("Kuznetsov", "Math", [
    ["-", "Math", "Math", "-", "-", "-", "-", "-"],
    ["Math", "Math", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["Math", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "Math", "-", "-", "-", "-", "-"]
])

inf_petrov = Teacher("Petrov", "Inf", [
    ["Inf", "Inf", "-", "-", "-", "-", "-", "-"],
    ["-", "Inf", "-", "-", "-", "-", "-", "-"],
    ["Inf", "-", "Inf", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["Inf", "-", "-", "-", "-", "-", "-", "-"]
])

geo_packerson = Teacher("Packerson", "Geo", [
    ["Geo", "Geo", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "Geo", "-", "-", "-", "-", "-"],
    ["Geo", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["Geo", "-", "-", "-", "-", "-", "-", "-"]
])

inf_smith = Teacher("Smith", "Inf", [
    ["-", "Inf", "-", "Inf", "-", "-", "-", "-"],
    ["Inf", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "Inf", "-", "-", "-", "-", "Inf", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "Inf", "-", "-", "-", "-", "-"]
])

teachers = [math_ivanov, math_kuznetsov, inf_petrov, geo_packerson, inf_smith]


def get_teacher():
    while True:
        name = input("Please input surname of the sick teacher: ")
        for i in teachers:
            if i.name.lower() == name.lower():
                return i
        print("There is no such teacher, please try again.")


def get_day():
    print("Work days:")
    print("1 - Monday")
    print("2 - Tuesday")
    print("3 - Wednesday")
    print("4 - Thursday")
    print("5 - Friday")

    while True:
        day = input("Input the required day of the week(1-5): ")
        if day.isdigit():
            day = int(day) - 1
            if day in range(5):
                return day
            else:
                print("Something went wrong with the day, please try again.")
        print("Please input digits!")


def get_lesson():
    while True:
        lesson = input("Input lesson (1-8): ")
        if lesson.isdigit():
            lesson = int(lesson) - 1
            if lesson in range(8):
                return lesson
            else:
                print("Something went wrong with the lesson, plesae try again.")
        print("Please input digits!")


def terminal():
    get_teacher()
    day = get_day()
    lesson = get_lesson()
    free_teachers = []

    for i in teachers:
        if i.teacher_is_free(day, lesson):
            free_teachers.append(i)

    if not free_teachers:
        print("Unfortunately there are no free teachers at this time.")
        return
    else:
        print("Teachers that are free at this time:")

    i = 1
    for t in free_teachers:
        print(str(i) + ". " + t.name + " (" + t.subject + ")")
        i = i + 1


start = input("Start program? (Please enter yes/no): ")
while start.lower() == "yes":
    terminal()
    start = input("Continue? (Please enter yes/no): ")
