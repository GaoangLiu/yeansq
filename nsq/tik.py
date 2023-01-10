from threading import Thread


class Tik(object):
    def __init__(self) -> None:
        self.cter = 0

    def tok(self):
        self.cter += 1

    def tak(self) -> bool:
        return not ((self.cter) & (self.cter - 1))


tik = Tik()
