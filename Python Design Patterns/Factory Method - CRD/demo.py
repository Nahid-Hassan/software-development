# Python Code for Object
# Oriented Concepts without
# using Factory method

class FrenchLocalizer:
    """ it simply returns the french version """

    def __init__(self):
        self.translations = {"car": "voiture",
                             "bike": "bicyclette", "cycle": "cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """ it simply returns the Spanish version """

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    """change the message using translations"""

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


if __name__ == "__main__":
    f = FrenchLocalizer()
    s = SpanishLocalizer()
    e = EnglishLocalizer()

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(s.localize(msg))
        print(e.localize(msg))
