"""
CP1404/CP5632 Practical 09
Band class
"""


class Band:
    """Band class with musicians and instruments."""

    def __init__(self, name=""):
        """Initialize Band with empty collections of musicians and instruments."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of Band."""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return play message."""
        play_message_lines = []
        for musician in self.musicians:
            if len(musician.instruments) != 0:
                play_message_lines.append(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                play_message_lines.append(f"{musician.name} needs an instrument!")
        return "\n".join(play_message_lines)


if __name__ == '__main__':
    from musician import Musician
    from guitar import Guitar

    band = Band()
    assert not band.name
    assert not band.musicians
    band.name = "Extreme"
    nuon = Musician("Nuno Bettencourt")
    nuon.instruments.append(Guitar("Washburn N4", 1990, 2499.95))
    nuon.instruments.append(Guitar("Takamine acoustic", 1986, 1200))
    band.musicians.append(nuon)
    gary_cherone = Musician("Gary Cherone")
    band.musicians.append(gary_cherone)
    pat_badger = Musician("Pat Badger")
    pat_badger.instruments.append(Guitar("Mouradian CS-74 Bass", 2009, 1500))
    band.musicians.append(pat_badger)
    kevin_figueiredo = Musician("Kevin Figueiredo")
    band.musicians.append(kevin_figueiredo)
    print(band)
