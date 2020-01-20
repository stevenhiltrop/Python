class School:
    def __init__(self):
        self.school = list()

    def add_student(self, name, grade):
        self.school.append((name, grade))

    def roster(self):
        students = list()

        for student in self.school:
            students.append(student[0])

        self.school.sort(key=comparator)
        return students

    def grade(self, grade_number):
        students = list()

        for student in self.school:
            if grade_number in student:
                students.append(student[0])

        return sorted(students)


def comparator(tuple_element):
    return tuple_element[1]
