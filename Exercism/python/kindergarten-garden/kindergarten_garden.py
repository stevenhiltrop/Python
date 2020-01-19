from enum import Enum


class Garden:
    def __init__(self, diagram, students=list()):
        if diagram:
            self.diagram = diagram.rplsit()
        if students:
            self.students = sorted(students)
        else:
            self.students = [
                "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
            ]

    def plants(self, name):
        pass


class Plant(Enum):
    Grass = "G"
    Clover = "C"
    Radishes = "R"
    Violets = "V"
