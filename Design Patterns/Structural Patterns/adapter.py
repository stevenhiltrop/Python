class Korean:
    def __init__(self):
        self.language = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class English:
    def __init__(self):
        self.language = "English"

    def speak_english(self):
        return "Hello?"


class Adapter:
    def __init__(self, object, **adapted_method):
        self.object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, item):
        return getattr(self.object, item)


objects = list()
korean = Korean()
english = English()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(english, speak=english.speak_english))

for object in objects:
    print(f"{object.language} says {object.speak()}")
