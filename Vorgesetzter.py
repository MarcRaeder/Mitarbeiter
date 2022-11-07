from mitarbeiter import Mitarbeiter


class Vorgesetzter(Mitarbeiter):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def setzeBestelllimit(self, limit: int) -> int:
        self._bestelllimit = limit
