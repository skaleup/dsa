from typing import List

def main(numbers: List[int], k=3) -> bool:
  max_sum = 0
  window_sum = 0
  numbers_length = len(numbers)
  if(numbers_length == 0):
    print("Array is empty")
  if(numbers_length < k):
    k = numbers_length  
  window_sum = sum(numbers[:k])
  for number_index in range(numbers_length - k ):
    window_sum = window_sum - numbers[number_index] + numbers[number_index + k]
    if(window_sum > max_sum):
      max_sum = window_sum
  print(max_sum)

if __name__ == "__main__":
  main([-2,1,-3,4,-1,2,1,-5,4])  
