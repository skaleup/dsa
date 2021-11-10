from typing import List

def main(numbers: List[int], k=3) -> bool:
  max_sum = 0
  window_sum = 0
  window_sum = sum(numbers[:k])
  for number in range(len(numbers) - k ):
    window_sum = window_sum - numbers
    if(window_sum > max_sum):
      max_sum = window_sum
  print("max sum")

if __name__ == "__main__":
  main()  
