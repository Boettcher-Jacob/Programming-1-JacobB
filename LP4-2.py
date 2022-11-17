def main():
  height = int(input("Please enter height = "))
  width = int(input("Please enter width = "))
  length = int(input("Please enter length = "))
  volume = (length * width * height)
  weight = int(input("Please enter weight = "))

  if weight > 27 and volume > 100000:
    print("Too Large & Too Heavy!")
  elif volume > 100000:
    print("Too Large!")
  elif weight > 27:
    print("Too Heavy!")
  else:
    print("Package Accepted!")
    print("Have a Good Day!")
  
    


if __name__ == "__main__":
  main()