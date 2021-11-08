def containsDuplicates(numbers: List[int]) -> bool:
  numbers_set = {}
  for number in numbers:
    if number in numbers_set:
      return True
    else:
      numbers_set.add(number)

if __name__ == "__main__":
  main()  
