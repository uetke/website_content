Virtual Environment is a Must-Have Tool
=======================================

:date: 2018-03-09
:status: draft
:author: Aquiles Carattino
:subtitle: Isolate different development environments from each other to avoid overlaps
:header: {attach}compartments.jpg
:og_description: Create different programming environments for different projects and avoid conflicts

When you start developing software, it is of utmost importance to have an isolated programming environment in which you can control precisely the packages installed. This will allow you, for example, to use experimental libraries without overwriting software that other programs use in your computer. Isolated environments allow you, for example, to update a package only within that specific environment, without altering the dependencies in every other development you are doing.

Python provides a very convenient tool called ``Virtual Environment`` that allows you to do exactly what was described. The instructions are slightly different depending on the operating system that you use, but they are easy to adapt from one to the other. To install ``Virtual Environment`` you can do it with ``pip``, the package manager of Python. Remember that sometimes you may have more than one version of pip in your computer, in the same way, you may have more than one version of Python. In the command line you run:

.. code-block:: bash

   pip3 install virtualenv

If you are on Linux, you may need to add ``sudo`` to the command: ``sudo pip3 install virtualenv``. This is the last installation that you do system-wide; from now on, everything else will happen within a `Virtual Environment`. We create a folder to hold all the needed files and initialize the environment.

.. code-block:: bash

   mkdir myproject
   cd myproject
   virtualenv venv -p python3

The first two lines create the folder and mode into it. In the last line, we create the virtual environment within a folder called ``venv`` and using a specific version of Python, ``python3``. On Linux you would do:

.. code-block:: bash

   source venv/bin/activate

while on Windows it would be:

.. code-block:: bash

   venv\Scripts\activate

If everything went well, you will see that a ``(venv)`` appears in at the beginning of the command line. Now you are working inside the Virtual Environment called ``venv`` and all the packages you install are going to be stored within it. Let's install a package to see how it works.

.. code-block:: bash

   pip install Flask==0.9

The command will install a very specific version of Flask, which is not the most recent one. One of the useful aspects of virtual environments is that they allow you to keep track of all the packages that you have installed, including their versions:

.. code-block:: bash

   pip freeze

You can output the results to a file that you can use later on for automatically installing all the requirements:

.. code-block:: bash

   pip freeze > requirements.txt

If you open the file ``requirements.txt`` you will notice that it contains a list with all the packages from ``venv``. To see the full potential of Virtual Environment, let's create a second one. First, we need to deactivate the one we are working on now by running:

.. code-block:: bash

   deactivate

And now we repeat the step above to create a new environment, but with a different name:

.. code-block:: bash

   virtualenv test -p python3

And we activate it:

.. code-block:: bash

   source test/bin/activate

or for Windows:

.. code-block:: bash

   venv\Scripts\activate

If we run again ``pip freeze`` you will notice that your environment is empty. We can install all the packages contained in the ``requirements.txt`` file by simply running:

.. code-block:: bash

   pip install -r requirements.txt

If you check again with ``pip freeze`` you will notice that you have exactly the same packages than in the ``venv`` environment. You can upgrade Flask, for example:

.. code-block:: bash

   pip install --upgrade Flask

And if you run again ``pip freeze`` you will notice that the version of Flask has changed. Repeat the steps mentioned above in order to deactivate ``test`` and activate ``venv``. You will see that the version of Flask stayed at ``0.9`` and was not upgraded.

Conclusions
^^^^^^^^^^^
It is almost impossible to overestimate how useful `Virtual Environment` is. It will help you stay organized and out of conflicts when you develop software, and it will also avoid problems when you are installing different libraries that you want to test. It doesn't matter if it is for the lab computer or for analyzing data, if you keep your programs compartmentalized, you can be sure that they will all run properly, regardless of their specific needs.

Remember, every time you are about to start a new project, regardless of what it is, you should start by creating an appropriate Virtual Environment for it. In this way, you can be certain of the long-term prosperity of the code you write, regardless of where it will bring you.

Header photo by `Michael Aleo <https://unsplash.com/photos/OsdgZG1byTk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`_ on Unsplash