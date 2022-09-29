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
    
  def fic(self) -> bool:
    """Front is Clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """Front is Blocked"""
    return not self.fic()

  def rib(self) -> bool:
    """Right is Blocked"""
    return not self.ric()

  def ric(self) -> bool:
    """Right is Cleared"""
    self.tr()
    if self.fic():
      self.tl()
      return True # Immedlately leaves the function
    self.tl
    return False
  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
  def o(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.put2()
  def o(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.put()
    pass

  def mm(self, num):
    for number in range(num):
      self.m()
  def pickm(self, num):
    for l in range(num-1):
      self.pick()
      self.m()
    self.pick()
  def putm(self, num):
    for l in range(num-1):
      self.put()
      self.m()
    self.put()
  def sob(self) -> bool:
    """Standing on Beeper""" 
    return beepers_present()

  def jump(self):
    """Jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
      """Find for 515"""
      while not facing_north():
        self.tl()
      self.m()
      if not self.sob():
        self.tl()
        self.m()
        self.tl()
        self.m()
      for _ in range(2):
        if not self.sob():
          self.m()
          self.tl()
          self.m()
      pass

def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.putm(9)
    kt.tl()
    kt.m()
    kt.putm(2)
    kt.tl()
    kt.m()
    kt.putm(8)
    kt.tl()
    kt.m()
    kt.put()
    pass


if __name__ == "__main__":
    run_karel_program()