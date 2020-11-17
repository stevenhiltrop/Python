import copy


class Prototype:
    def __init__(self):
        self._objects = dict()

    def register_object(self, name, object):
        self._objects[name] = object

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attributes):
        object = copy.deepcopy(self._objects.get(name))
        object.__dict__.update(attributes)
        return object


class Car:
    def __init__(self):
        self.name = "Sky Lark"
        self.color = "Red"
        self.option = "Ex"

    def __str__(self):
        return f"{self.name} | {self.color} | {self.option}"


car = Car()
prototype = Prototype()
prototype.register_object("skylark", car)

car_copy = prototype.clone("skylark")
print(car_copy)