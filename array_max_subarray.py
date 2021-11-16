from typing import List

def main(numbers: List[int], k=3) -> bool:
  max_sum = numbers[0]
  sum_till_here = 0
  numbers_length = len(numbers)
  if(numbers_length == 0):
    print("Array is empty")
  for number in numbers:
    sum_till_here = sum_till_here + number
    if(sum_till_here > max_sum):
      max_sum = sum_till_here
    if(sum_till_here < 0):
      sum_till_here = 0
  print(max_sum)

if __name__ == "__main__":
  main([-2,1,-3,4,-1,2,1,-5,4])  
