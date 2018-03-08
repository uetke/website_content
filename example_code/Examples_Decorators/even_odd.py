import math

def even_odd_average(x, y):
   def average(a, b):
      return (a+b)/2

   def geom_average(a, b):
      return math.sqrt(a*b)
   if (x+y) % 2 == 0:
      return average(x, y)
   else:
      return geom_average(x, y)

print(even_odd_average(4, 6))
print(even_odd_average(4, 9))
