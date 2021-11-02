def main():
  a = int(raw_input().strip())
  b = int(raw_input().strip())
  if(b != 0):
    print(a//b)
    print(a/b)
  else:
    print("Denominator can not be Zero")

if __name__ == "__main__":
  main()  
