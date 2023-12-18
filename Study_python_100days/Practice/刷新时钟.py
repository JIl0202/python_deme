from time import sleep


class Clocks(object):
    def __init__(self, a, b, c, d):
        self.A = a
        self.B = b
        self.C = c
        self.D = d

    def run(self):
        self.D += 1
        if self.D == 60:
            self.D = 0
            self.C += 1
            if self.C == 60:
                self.C = 0
                self.B += 1
                if self.B == 24:
                    self.B = 0
                    aa = self.A
                    self.A %= 100
                    self.A += 1
                    aa //= 100
                    self.A = 100 * aa + self.A

    def now(self):
        return "%06d.%02d:%02d:%02d" % (self.A, self.B, self.C, self.D)


if __name__ == '__main__':
        Clock = Clocks(20230602, 23, 59, 57)
        while True:
            print('\r', Clock.now(), end='', flush=True)
            sleep(1)
            Clock.run()



