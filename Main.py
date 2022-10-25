from Mitarbeiter import Mitarbeiter
from Vorgesetzter import Vorgesetzter


def main() -> None:
    walterWinkelmann: Mitarbeiter = Mitarbeiter("Walter Winkelmann")
    waltraudWichtig: Vorgesetzter = Vorgesetzter("Waltraud Wichtig")
    hermannWichtiger: Vorgesetzter = Vorgesetzter("Hermann Wichtiger")
    walterWinkelmann.setVorgesetzten(waltraudWichtig)
    waltraudWichtig.setVorgesetzten(hermannWichtiger)
    print(walterWinkelmann.darfBestellen(15))
    print(walterWinkelmann.darfBestellen(20))
    print(walterWinkelmann.darfBestellen(21))
    print(hermannWichtiger.darfBestellen(15))
    print(hermannWichtiger.darfBestellen(25))
    walterWinkelmann.setAllgemeinesLimit(30)
    print(walterWinkelmann.getBestelllimit())
    williWinzig = Mitarbeiter("Willi Winzig")
    print(walterWinkelmann.darfBestellen(21))
    print(hermannWichtiger.darfBestellen(25))
    waltraudWichtig.setBestelllimit(10)
    print(waltraudWichtig.getBestelllimit())
    print(waltraudWichtig.darfBestellen(10))
    print(waltraudWichtig.darfBestellen(11))
    waltraudWichtig.setBestelllimit(5000)
    print(waltraudWichtig.darfBestellen(2000))
    print(waltraudWichtig.darfBestellen(7000))
    waltraudWichtig.gibInfo()
    walterWinkelmann.gibHierarchie(walterWinkelmann)
    hermannWichtiger.gibInfo()
    hermannWichtiger.gibHierarchie(hermannWichtiger)
    walterWinkelmann.gibInfo()
    walterWinkelmann.gibHierarchie(walterWinkelmann)
    waltraudWichtig.setVorgesetzten(None)
    walterWinkelmann.gibHierarchie(walterWinkelmann)
    williWinzig.gibInfo()
    williWinzig.gibHierarchie(williWinzig)


if __name__ == '__main__':
    main()
