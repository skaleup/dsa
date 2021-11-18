from typing import List

def main(numbers: List[int], target: int) -> bool:
  result = []
  for index, number in enumerate(numbers):
    try:
      second_index = numbers.index(target - number)
      if(index != second_index):
        result = [index, second_index]
        break
    except:
      continue
  return result        

if __name__ == "__main__":
  main([2,7,11,15], 9)  
