class Subject:
    def __init__(self):
        self._observers = list()

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            raise ValueError(f"Could not find {observer}")

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update()


class Core(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
        Subject.notify(self)
