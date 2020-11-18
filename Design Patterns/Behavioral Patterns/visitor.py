class House:
    def accept(self, visitor):
        pass

    def work_on_hvac(self, hvac_specialist):
        print(f"{self} worked on by {hvac_specialist}")

    def work_on_electricity(self, electrician):
        print(f"{self} worked on by {electrician}")

    def __str__(self):
        return self.__class__.__name__


class Visitor:
    def __str__(self):
        return self.__class__.__name__


class HVACSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)
