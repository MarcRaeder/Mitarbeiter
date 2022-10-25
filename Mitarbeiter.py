from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Vorgesetzter import Vorgesetzter


class Mitarbeiter:

    _bestelllimit: int = 20
    _vorgesetzter: Vorgesetzter = None

    def __init__(self, name) -> None:
        self._name: str = name

    @classmethod
    def setAllgemeinesLimit(cls, limit: int) -> int:
        cls._bestelllimit: int = limit
        return cls._bestelllimit

    def setVorgesetzten(self, name: Vorgesetzter) -> Vorgesetzter:
        self._vorgesetzter = name
        return name

    def setName(self, name: str) -> str:
        self._name = name

    def getName(self) -> str:
        return self._name

    def getVorgesetzten(self) -> Vorgesetzter:
        if self._vorgesetzter == None and self.__class__.__name__ == "Mitarbeiter":
            print("freier Mitarbeiter")
        elif self._vorgesetzter == None:
            print("Es wurde kein Vorgesetzter zugewiesen")
        elif self._vorgesetzter is not None:
            return self._vorgesetzter

    def getBestelllimit(self) -> int:
        return self._bestelllimit

    def darfBestellen(self, beschaffung: int) -> bool:
        if beschaffung <= self._bestelllimit:
            return True
        elif beschaffung > self._bestelllimit:
            return False

    def gibInfo(self):
        if self._vorgesetzter is not None:
            print(
                f"Ich bin {self.__class__.__name__}, Name {self.getName()}. Mein Vorgesetzter ist {self._vorgesetzter.getName()}. Mein Bestelllimit ist {self.getBestelllimit()} EUR. ")
        elif self._vorgesetzter == None and self.__class__.__name__ == "Mitarbeiter":
            print(
                f"Ich bin freier Mitarbeiter, Name {self.getName()}. Mein Bestelllimit ist {self.getBestelllimit()} EUR. ")
        else:
            print(
                f"Ich bin {self.__class__.__name__}, Name {self.getName()}. Mein Bestelllimit ist {self.getBestelllimit()} EUR. ")

    def gibHierarchie(self, mitarbeiter: Mitarbeiter) -> str:
        if self._vorgesetzter == None and self.__class__.__name__ == "Mitarbeiter":
            print(f"freier Mitarbeiter {self.getName()}")
        else:
            hierarchie = []
            chef = mitarbeiter.getVorgesetzten()

            while True:
                try:
                    chefdata = f"{chef.__class__.__name__} {chef.getName()}"
                    hierarchie.insert(0, chefdata)
                    chef = chef.getVorgesetzten()

                except AttributeError:
                    break

            for element in hierarchie:
                print(element)
            print(f"{self.__class__.__name__} {self.getName()}")
