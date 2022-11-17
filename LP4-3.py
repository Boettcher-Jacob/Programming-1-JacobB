def main(): 

  Eggs = int(input("Please Input Eggs = "))
  Dozens = Eggs / 12

if Dozens >= 0 and Dozens < 4:
  Price = Dozens * .50
elif Dozens >= 4 and Dozens < 6:
  Price = Dozens * .45
elif Dozens >= 6 and Dozens < 11:
  Price = Dozens * .40
elif Dozens >= 11:
  Price = Dozens * .35
else:
  Bonus = Eggs - Dozens
  