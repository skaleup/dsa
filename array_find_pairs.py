def main():
  number_of_socks = int(input().strip())
  sock_colors = list(map(str, input().split(' ')))
  sock_colors.sort()
  colors = {}
  total_pairs = 0
  if(number_of_socks < 1 or number_of_socks > 100):
    print("Number of socks has to be between 1 and 100")
  for color in sock_colors:
    if(int(color) < 1 or int(color) > 100):
      print("Color of sock has to be between 1 and 100")
    count = colors.get(color, 0)
    colors[color] = count + 1
    color_count = colors[color]
    if(color_count > 1 and (color_count % 2 == 0)):
      total_pairs += 1
  print(total_pairs)

if __name__ == "__main__":
  main()  
