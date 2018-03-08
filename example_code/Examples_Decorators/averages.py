import math

def average(x, y):
   if x<0 or y<0:
      raise Exception("Both x and y have to be positive")

   avg = (x + y)/2
   return avg

def geom_average(x, y):
   if x<0 or y<0:
      raise Exception("Both x and y have to be positive")

   avg = math.sqrt(x*y)
   return avg

def integer_output(func, x, y):
   res = func(x, y)
   return int(res)


rounded = integer_output(average, 1, 2)
print(rounded)
