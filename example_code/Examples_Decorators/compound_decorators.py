import math
import time

def timing_average(func):
    def wrapper(x, y):
        t0 = time.time()
        res = func(x, y)
        t1 = time.time()
        print("It took {} seconds for {} to calculate the average".format(t1-t0, func.__name__))
        return res

    return wrapper

def check_positive(func):
   def func_wrapper(x, y):
      if x<0 or y<0:
         raise Exception("Both x and y have to be positive for {} to work".format(func.__name__))
      res = func(x,y)
      return res
   return func_wrapper

@timing_average
@check_positive
def average(x, y):
   return (x + y)/2

@timing_average
@check_positive
def geom_average(x, y):
   return math.sqrt(x*y)


x = 9
y = 25

print("The average between {} and {} is {}".format(x, y, average(x, y)))
print("The geometrical average between {} and {} is {}".format(x, y, geom_average(x, y)))