from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vorgesetzter import Vorgesetzter


class Mitarbeiter:

    _bestelllimit: int = 20
    _vorgesetzter: Vorgesetzter = None

    def __init__(self, name) -> None:
        self._name: str = name

    @classmethod
    def setzeAllgemeinesLimit(cls, limit: int) -> int:
        cls._bestelllimit: int = limit
        return cls._bestelllimit

    def setzeVorgesetzten(self, name: Vorgesetzter) -> Vorgesetzter:
        self._vorgesetzter = name
        return name

    def setzeName(self, name: str) -> str:
        self._name = name

    def bekommeName(self) -> str:
        return self._name

    def bekommeVorgesetzten(self) -> Vorgesetzter:
        if self._vorgesetzter == None and self.__class__.__name__ == "Mitarbeiter":
            print("freier Mitarbeiter")
            return None
        elif self._vorgesetzter == None:
            print("Es wurde kein Vorgesetzter zugewiesen")
            return None
        elif self._vorgesetzter is not None:
            return self._vorgesetzter

    def bekommeBestelllimit(self) -> int:
        return self._bestelllimit

    def darfBestellen(self, beschaffung: int) -> bool:
        if beschaffung <= self._bestelllimit:
            return True
        if beschaffung > self._bestelllimit:
            return False

    def gibInfo(self):
        if self._vorgesetzter is not None:
            print(
                f"Ich bin {self.__class__.__name__}, Name {self.bekommeName()}. Mein Vorgesetzter ist {self._vorgesetzter.bekommeName()}. Mein Bestelllimit ist {self.bekommeBestelllimit()} EUR. "
            )
            return
        if self._vorgesetzter == None and self.__class__.__name__ == "Mitarbeiter":
            print(
                f"Ich bin freier Mitarbeiter, Name {self.bekommeName()}. Mein Bestelllimit ist {self.bekommeBestelllimit()} EUR. "
            )
            return

        print(
            f"Ich bin {self.__class__.__name__}, Name {self.bekommeName()}. Mein Bestelllimit ist {self.bekommeBestelllimit()} EUR. "
        )

    def gibHierarchie(self, mitarbeiter: Mitarbeiter) -> str:
        if self._vorgesetzter == None and self.__class__.__name__ == "Mitarbeiter":
            print(f"freier Mitarbeiter {self.bekommeName()}")
        else:
            hierarchie = []
            chef = mitarbeiter.bekommeVorgesetzten()

            while True:
                try:
                    chefdata = f"{chef.__class__.__name__} {chef.bekommeName()}"
                    hierarchie.insert(0, chefdata)
                    chef = chef.bekommeVorgesetzten()

                except AttributeError:
                    break

            for element in hierarchie:
                print(element)
            print(f"{self.__class__.__name__} {self.bekommeName()}")
