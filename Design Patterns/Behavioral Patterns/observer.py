class Subject:
    def __init__(self):
        self._observers = list()

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            raise ValueError(f"Could not find {observer}")

    def notify(self, modifier=None):
        for observer in self._observers:
            pass
