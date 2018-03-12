import math, time

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

def timing_average(func):
   def wrapper(x, y):
      t0 = time.time()
      res = func(x, y)
      t1 = time.time()
      print("It took {} seconds for {} to calculate the average".format(t1-t0, func.__name__))
      return res

   return wrapper

new = timing_average(average)
new(2, 4)

#### Syntactic Sugar ####

@timing_average
def new_average(x, y):
    return (x+y)/2


new_average(3, 5)