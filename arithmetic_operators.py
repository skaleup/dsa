def main():
  a = int(raw_input().strip())
  b = int(raw_input().strip())
  if((1 <= a <= pow(10, 10)) and (1 <= b <= pow(10, 10))):
    print(a+b)
    print(a-b)
    print(a*b)
  else:
    print("Number out of range")

if __name__ == "__main__":
  main()  
