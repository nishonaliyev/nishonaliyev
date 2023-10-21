from championship import Championship
class Gp:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    def getposition(self):
        for i in self.driver_list:
            return i
