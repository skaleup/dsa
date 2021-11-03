def main():
  number_of_socks = int(raw_input().strip())
  sock_colors = list(map(int, input().rstrip().split()))
  for color in sock_colors:
    print(color)

if __name__ == "__main__":
  main()  
