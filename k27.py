from stanfordkarel import *


class ktools:
  def m(self):
    """Short hand move"""
    move()

  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put Two"""
    put_beeper()
    move()
    put_beeper()

  def put5(self):
    """Put Five"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Letter H w/ Beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def e(self):
    self.tl()
    self.put5()
    self.tr()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    """Letter E w/ Beepers"""
    self.tl()
    self.put
  def m5(self):
    self.m()
    self.m()
    self.m()
    self.m()
    self.m()
def main():
    """ Karel code goes here! """
    kt=ktools()

    kt.m()
    kt.tl()
    kt.m5()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.pick()
    kt.m()
    kt.tl()
    kt.m()
    kt.pick()
    kt.m()
    kt.m()
    pass


if __name__ == "__main__":
    run_karel_program()