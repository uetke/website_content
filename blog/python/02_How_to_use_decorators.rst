How to use decorators to validate inputs
========================================

:date: 2018-03-12
:status: draft
:author: Aquiles Carattino
:subtitle: Decorators are useful, but can be hard to understand
:header: {attach}compartments.jpg
:og_description: Learn how to use decorators to validate user input before communicating with a device

Python is rich in resources that can shorten the time it takes to develop new programs and simplify repetitive tasks. Decorators are one of such elements but more often than not they are not considered by less experienced developers. Adding decorators to the syntactic toolbox can be of great use in different contexts, but in this article we are going to discuss how can they help you when communicating with a device.

Decorators in Python are nothing more than functions that take as arguments other functions. They appear with an ``@`` in front of them right above a function (or a method within a class). Let's quickly recap how functions work in Python and how to use them. Imagine you want to compute the average of two values. We can develop a function for it:

.. code-block:: python

   def average(x, y):
      avg = (x+y)/2
      return avg

We can use the function directly in our code by writing:

.. code-block:: python

   a = 1
   b = 3
   result = average(1, 3)
   print(result)

What you should see happening is that when you call the function ``average`` it adds both numbers and returns its mean value. Imagine that, for some reason, you want to allow only positive numbers as arguments of your function. You could expand your ``average`` function to check weather it is true or not.

.. code-block:: python

   def average(x, y):
      if x<0 or y<0:
         raise Exception("Both x and y have to be positive")

      avg = (x + y)/2
      return avg

Every time a user wants to use the function with a negative argument, an error will be raised. Now we develop a new function to compute the geometric average of two numbers, and we again need them both to be positive. Our function would look like:

.. code-block:: python

   import math

   def geom_average(x, y):
      if x<0 or y<0:
         raise Exception("Both x and y have to be positive")

      avg = math.sqrt(x*y)
      return avg

There is a general rule of thumb that says that code shouldn't be copied more than twice. If you are going to copy-paste code for a third time there is probably a better way of doing it. In the examples above, you can see that the verification of the input is exactly the same in both functions. If we were to write a third function, we would meet the three-copies rule. It would be useful to have an external way of checking that both inputs are positive, exactly what a decorator can do.

Functions as arguments and as results of other functions
********************************************************
Before we can go into the details of how to use ``decorators`` in Python, it is important to show how functions work with inputs and outputs that are other functions. For example, we could define a function that transforms the output of the averages defined above into integers. It is a simple example, but shows the pattern that you can follow in order to achieve a more complex behavior.

.. code-block:: python

   def integer_output(func, x, y):
      res = func(x, y)
      return int(res)

You can see that ``integer_output`` takes three arguments, a function ``func`` and two numbers, ``x`` and ``y`` . We use the function, regardless of what it is, with arguments ``x`` and ``y``. It returns the result converted to an integer value. We can use the function like this:

.. code-block:: python

   rounded = integer_output(average, 1, 2)
   print(rounded)
   geom_rounded = integer_output(geom_average, 4, 5)
   print(geom_rounded)

It is important to note that the first argument is a function and it doesn't matter which one. You could use ``average`` or ``geom_average``. The next two arguments are going to be passed directly to ``func`` . This is already quite powerful and most likely you can think a lot of ways in which you can use it, but Python allows you to do even more interesting things.

Functions can also be defined within functions and you can use them based in your input arguments. For example, let's assume you want to use ``average`` only if the sum of x and y is even and the ``geom_average`` if the sum is odd:

.. code-block:: python

   def even_odd_average(x, y):
      def average(a, b):
         return (a+b)/2
      def geom_average(a, b):
         return math.sqrt(a*b)

      if (x+y) % 2 == 0:
         return average(x, y)
      else:
         return geom_average(x, y)

The function ``even_odd_average`` takes only two arguments on which it is going to perform the average. Inside we define two functions, exactly as we did a the beginning, ``average`` and ``geom_average``, but this time they are available only within the ``even_odd_average`` function. Based on the input we either calculate the average or the geometric average as requested earlier and we return the value. We can use this function as:

.. code-block:: python

   print(even_odd_average(4, 6))
   print(even_odd_average(4, 9))

So far, we have seen how to use functions as arguments in other functions and how to define functions within functions. The only missing part is to be able to return a function and not a value. Let's assume you want to print the time it takes to calculate the average between two numbers, but you don't want to re-write your original function. We have to write what is called a function wrapper.

.. code-block:: python

   import time

   def timing_average(func):
      def wrapper(x, y):
         t0 = time.time()
         res = func(x, y)
         t1 = time.time()
         print("It took {} seconds to calculate the average".format(t1-t0))
         return res

      return wrapper

We start by defining a function that takes as an argument another function. We also define a new function called ``wrapper`` as we explained earlier. So far, both steps were done in the previous examples, but now we are going to use ``func`` within the ``wrapper``. We start by storing the current time at the variable ``t0``. We execute the function ``func`` with the arguments ``x`` and ``y`` and store the new time at ``t1``. We print the total time it took to run the function and return the output of ``func``. The important part here is the very last line. As you can see, we are not returning the value that ``func`` returns, but we are actually returning the ``wrapper``, which is in itself a function. To see this in action, we can do the following:

.. code-block:: python

   new = timing_average(average)
   new(2, 4)

What you see in the above code is that we create a function called ``new`` by using ``timing_average`` with only argument the function ``average``. ``New`` will take the same inputs that the ``wrapper`` function takes. If we use ``new`` as a function, with arguments ``2`` and ``4`` , you will see that it prints to screen the total time it took to calculate the average. New is nothing more than the function ``wrapper``, defined using ``average``. We could do the same using ``geom_average``.

The syntax above can be hard to understand and forces you to define new functions if you want to add timing capabilities. When you see that you are assigning the output of ``timing_average`` to a variable called ``new`` you don't expect it to actually be a function. If you already have working code, you need to do a lot of refactoring in order to define and use the new functions.

Fortunately, Python offers a very clear and simple way of achieving the same functionality, without the downsides just exposed. If you managed to follow the above examples, you are ready to improve the way the code looks by using decorators.

Introducing Decorators
**********************
You already know everything there is to know regarding how to use decorators, you are just missing the syntactic sugar of Python. Coming back to the examples of the averages that take only positive arguments, and using the example of ``timing_average``, we can develop a wrapper function that would check weather the input of our function is positive or not.

.. code-block:: python

   def check_positive(func):
      def func_wrapper(x, y):
         if x<0 or y<0:
            raise Exception("Both x and y have to be positive for function {} to work".format(func.__name__))
         res = func(x,y)
         return res
      return func_wrapper

The structure of ``check_positive`` is very similar to what we have done for the timing. The only difference is that we check the input arguments and we raise an ``Exception`` if they are not both positive. Since we are raising an exception for an unknown function, it becomes handy to display which function actually gave the error. The rest is exactly the same as with the timing example. What we are going to do now is to show how to use it as a decorator. We can write our averages functions as follows:

.. code-block:: python

   @check_positive
   def average(x, y):
      return (x + y)/2

   @check_positive
   def geom_average(x, y):
      return math.sqrt(x*y)

Both functions, ``average`` and ``geom_average`` don't change their names, therefore you can use them as always, but now they check for positive input before computing the average. You can use them as always:

.. code-block:: python

   average(2, 4)
   average(-2, 4)

Decorators are very powerful and can help you develop very clean and useful code. The obvious use of decorators is to validate input when it is the user providing it. Decorators are also very useful when you are writing a library that other developers are going to use. When we discussed `how to control a device over the network <{filename}how_to_control_network.rst>`_, we have used the ``@route`` decorators provided by ``Flask``. We have also used decorators when we have `introduced Lantz <{filename}introducing_lantz.rst>`_.

One of the advantages of decorators is that even if a developer doesn't fully understand what is happening under the hood, it will for sure understand how to use them and what to expect. If you provide good examples in your code it will become apparent where and when to include specific decorators. Now that you have a basic understanding of what the ``@`` means in Python you can start thinking about many more interesting applications. 

