How to use HDF5 files in Python
===============================

:date: 2018-03-19
:status: draft
:author: Aquiles Carattino
:subtitle: HDF5 allows you to store large amounts of data efficiently
:header: {attach}compartments.jpg
:og_description: Learn how to use the HDF5 format to store large amounts of data and read it back with Python

When dealing with large amounts of data, both in the lab or as result of simulations, saving to text files is not going to work. Sometimes you need to access a very specific subset of data and you want to do it fast. The HDF5 format solves both issues thanks to a very optimized underlying library. It is broadly used in scientific environments and has a great implementation in Python, designed to work with numpy out of the box. In this article we are going to see how you can use it to store data to a hard drive and how you can retrieve it later on.

The HDF5 format is supported by the `HDF Group <https://www.hdfgroup.org/>`_, it is based on open source standards, meaning that your data will always be accessible, even if the group disappears. Support for Python is given through the `h5py package <https://www.h5py.org/>`_ that can be installed through ``pip``. Remember that you should be using a `virtual environment <{filename}01_Virtual_Environment.rst>`_ to perform tests:

.. code-block:: shell

   pip install h5py

the command will also install numpy in case you don't have it already in your environment.

Let's go straight to it. We will create a new file and save a numpy random array to it.

.. code-block:: python

   import h5py
   import numpy as np

   arr = np.random.randn(1000)

   with h5py.File('random.hdf5', 'w') as f:
       dset = f.create_dataset("default", data=arr)


The first few lines are quite straightforward, we import the needed packages and create an array with random values. We open a file called `random.hdf5` with ``w`` , which means that if there is a file with the same name it is going to be overwritten. We create a `dataset` called ``default`` and we set the data to the random array created earlier. Datasets are holders for our data, basically the building blocs of the HDF5 format. Since we are working with the ``with`` statement, we don't need to close the file, but if you are doing it differently, don't forget to add ``f.close()`` at the end.

To read the data back, we can do it in a very similar way to how you would read a numpy file.

.. code-block:: python

   with h5py.File('random.hdf5', 'r') as f:
      data = f['default']
      print(min(data))
      print(max(data))

We first open the file with a read attribute ``r`` and we recover the data by directly addressing the dataset called `default` that we created earlier. Now we have the data available to do whatever we want, for example displaying the maximum and minimum values in the array. However, in these simple commands there are several things going on under the hood that get very often overlooked in other guides.

In the code above, you can use ``data`` as a normal array. You can, for example address the third element by doing ``data[2]``, our you could get a range of values with ``data[1:3]``. However, data is not an array but a dataset. You can see it by adding ``print(type(data))`` after the print statement. Datasets work in a completely different way than arrays, because their information is stored on the hard drive and they don't load to RAM until we don't use them. The following code, for example, will not work:

.. code-block:: python

   f = h5py.File('random.hdf5', 'r')
   data = f['default']
   f.close()
   print(data[1])

The error appears a bit lengthy, but the last line is very helpful:

.. code-block:: shell

   ValueError: Not a dataset (not a dataset)

It means that we are trying to access a dataset to which we have no longer access. It is confusing, but since we closed the file, when we try to print the second value in data we are not allowed. When we assigned ``f['default']`` to the variable ``data`` we are not actually reading the file, we are just generating a pointer to where the data is located.

The behavior would be completely different if we specify a range for our data, for example:

.. code-block:: python
   :hl_lines: 2

   f = h5py.File('random.hdf5', 'r')
   data = f['default'][:10]
   f.close()
   print(data[1])

The highlighted line is different, we are now explicitly addressing the first 10 elements of the dataset and we are storing them into the ``data`` variable. Even if we close the file, the information is still available because it was read and stored into the RAM memory. You could have read the entire array by using ``[:]``, for example.

It is up to you to decide if you want to read the entire array into memory or not. When you are dealing with very large datasets, perhaps you can't afford to read all the information because the memory is not enough. The same principle is applied when you write data to an hdf5 file. Let's re write the example above to see how this works.

.. code-block:: python

   f = h5py.File('random.hdf5', 'w')
   dset = f.create_dataset("default", (1000,))
   dset[10:20] = arr[50:60]
   f.close()

The first few lines are the same, but now we don't append data when creating the dataset. We just create a dataset able to hold 1000 elements. We are actually writing to disk when we assign elements to the ``dset`` variable. In the example above we assign values just to a subset of the array, the indexes from 10 to 19.

.. warning:: It is not entirely true that you write to disk when you assign values to a dataset. The precise moment depends on several factors, including the state of the operating system. If the program closes too early, it may be that not everything was written. It is very important to always use the ``close()`` method, and in case you write in stages, you can also use ``flush()`` in order to force the writing.

If you read the file again and print the first 20 values of the dataset, you will see that they are all zeros except for the indexes 10 to 19.

So far, we have covered only the tip of the iceberg of what HDF5 has to offer. Besides to the length of the data you want to store, you may want to specify the type of data in order to optimize the space and speed. The `h5py documentation <http://docs.h5py.org/en/latest/faq.html>`_ provides a list of the supported types, we are going show here just a couple of them. We are also going to work with several datasets in the same file, at the same time.

.. code-block:: python

   with h5py.File('several_datasets.hdf5', 'w') as f:
      dset_int_1 = f.create_dataset('integers', (10, ), dtype='i1')
      dset_int_8 = f.create_dataset('integers8', (10, ), dtype='i8')
      dset_complex = f.create_dataset('complex', (10, ), dtype='c16')

      dset_int_1[0] = 1200
      dset_int_8[0] = 1200.1
      dset_complex[0] = 3 + 4j

In the example above, we have created three different datasets, each with a different type. Integers of 1 byte, integers of 8 bytes and complex numbers of 16 bytes. We are storing only one number, even if our datasets can hold up to 10 elements. You can read the values back and see how they were stored. The two things to note are that the integer of 1 byte should have been rounded to 127 (instead of 1200) and the integer of 8 bytes should have been rounded to 1200 (instead of 1200.1).

Depending on your background, perhaps you haven't thought before what is the impact that specifying datatypes may have, so let's see it with a simple example. Let's create three files, with one dataset for 100000 elements each but with different data types, and then we can compare the size of each. We have to create a random array to assign to each dataset in order to fill the memory.

.. code-block:: python

   arr = np.random.randn(100000)

   f = h5py.File('integer_1.hdf5', 'w')
   d = f.create_dataset('dataset', (100000,), dtype='i1')
   d[:] = arr
   f.close()

   f = h5py.File('integer_8.hdf5', 'w')
   d = f.create_dataset('dataset', (100000,), dtype='i8')
   d[:] = arr
   f.close()

   f = h5py.File('float.hdf5', 'w')
   d = f.create_dataset('dataset', (100000,), dtype='f16')
   d[:] = arr
   f.close()

If you check the size of each of the files you will get something like:

========= ========
File      Size (b)
--------- --------
integer_1 102144
integer_8 802144
float     1602144
========= ========

The impact in size is quite obvious. When you go from 1 byte to 8 bytes the size of the file increases 8-fold, and when you go to 16 bytes it takes approximately 16 times more space. The space it takes to store data is not the only important factor to take into account, you also have to consider the time it takes to write the data to disk. The more you have to write, the longer it will take. Depending on your application it may be crucial to use the specific type that describes your data. In the lab it may happen that you need to write to disk while you acquire and you need to optimize the procedure as much as possible in order not to run out of memory.

Remember that when you initialize an array with numpy it will default to 8 bytes (64 bits) per element. If you store the data to hdf5 directly when creating the dataset it will do it as ``'f8'``, which may or may not be what you want. It is also the explanation of why it takes twice as much memory in the disk, we saved it as 16 bytes (``'f16'``) while the data was  8 bytes.