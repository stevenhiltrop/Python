import collections


class School:
    def __init__(self, school=""):
        self.school = collections.defaultdict(list)
        self.name = school

    def add_student(self, name, grade):
        self.school[grade].append(name)

    def roster(self):
        school = [self.grade(grade) for grade in sorted(self.school.keys())]
        return [child for _class in school for child in _class]

    def grade(self, grade_number):
        return sorted(self.school[grade_number])