from typing import List

def main(numbers: List[int]) -> bool:
  numbers_set = set()
  for number in numbers:
    if number in numbers_set:
      return True
    else:
      numbers_set.add(number)
  return False
  
if __name__ == "__main__":
  print(main([1,2,3]))
