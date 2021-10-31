def main():
  number = int(raw_input("Enter a number: ").strip())
  if(number < 1 or number > 100):
    print("Number must be between 1 and 100")
  elif(number % 2 == 1):
    print("Weird")
  elif(6 <= number <= 20):
    print("Weird")
  else:
    print("Not Weird")

if __name__ == "__main__":
  main()  
