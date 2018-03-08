import math

def check_positive(func):
   def func_wrapper(x, y):
      if x<0 or y<0:
         raise Exception("Both x and y have to be positive for {} to work".format(func.__name__))
      res = func(x,y)
      return res
   return func_wrapper

@check_positive
def average(x, y):
   return (x + y)/2

@check_positive
def geom_average(x, y):
   return math.sqrt(x*y)


print(average(1, 3))
print(average(-1, 3))
print(geom_average(4, 9))
print(geom_average(-4, 9))