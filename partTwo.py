import math  

def main():
  a = int(input("What's the value of side A? "))
  b = int(input("What's the value of side B? "))
  c = pythag(a, b)
  print(c)

def pythag(A,B):
  return math.sqrt(A ** 2 + B ** 2)

main()
