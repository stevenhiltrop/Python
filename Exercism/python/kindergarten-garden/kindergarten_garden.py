class Garden:
    def __init__(self, diagram, students=list()):
        self.plant = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

        if diagram:
            self.diagram = diagram.rsplit()
        if students:
            self.students = sorted(students)
        else:
            self.students = [
                "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
            ]

    def plants(self, student_name):
        student_index = self.students.index(student_name)
        student_plants = list()

        for row in range(2):
            student_plants.append(self.diagram[row][student_index * 2])
            student_plants.append(self.diagram[row][student_index * 2 + 1])

        return [self.plant[p] for p in student_plants]
