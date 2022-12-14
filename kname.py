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
    self.put()
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.put()
  def zero(self):
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
  def j(self):
    self.put2()
    self.tl()
    self.m()
    self.putm(4)
    self.tl()
    self.m()
    self.put()
    self.ta()
    self.mm(2)
    self.put()
  def a(self):
    self.putm(3)
    self.tr()
    self.m()
    self.putm(4)
    self.tr()
    self.mm(2)
    self.tr()
    self.putm(3)
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.put()
  def c(self):
    self.putm(3)
    self.tr()
    self.mm(4)
    self.tr()
    self.putm(3)
    self.tr()
    self.m()
    self.putm(3)
  def b(self):
    self.put5() # Start of B
    self.tr()
    self.m()
    self.tr()
    self.put()
    self.mm(2)
    self.put()
    self.mm(2)
    self.put()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.mm(2)
    self.put()
def main():
    """ Karel code goes here! """
    kt=ktools()
    pass
    kt.j()
    kt.mm(2)
    kt.a()
    kt.m()
    kt.tr()
    kt.mm(4)
    kt.c()
    kt.m()
    kt.tr()
    kt.mm(4)
    kt.tr()
    kt.mm(4)
    kt.tl()
    kt.o()
    kt.ta()
    kt.mm(3)
    kt.tl()
    kt.b()
    kt.mm(3)


if __name__ == "__main__":
    run_karel_program()