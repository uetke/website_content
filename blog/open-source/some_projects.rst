Some Open Source Projects Worth Checking
========================================

:subtitle: Get inspiration from some of the best resources available online
:og_description: Collection of open source packages to learn how to develop your own code
:date: 2018-02-27
:header: {attach}science_cern.jpg

Some days ago, we have discussed if it was worth `moving projects to the open source community <{filename}../open-source/should_labs_move_to_open_source.rst>`_. Therefore we believe that it is important to show some of the already available projects in order to have an idea of what can be done and where to find inspiration. Not all projects are equally mature, but they are all a great starting point for further developments.

Storm Control - Zhuang Lab
^^^^^^^^^^^^^^^^^^^^^^^^^^
`Storm Control <https://github.com/ZhuangLab/storm-control>`_ is a platform for controlling a microscope to acquire `Storm Images <https://www.microscopyu.com/tutorials/stochastic-optical-reconstruction-microscopy-storm-imaging>`_. It is built on Python and Qt5, the same core technologies we use for the developments of Uetke. Even if you are not interested in super resolution, you should keep an eye on this project, since it provides a lot of `drivers <https://github.com/ZhuangLab/storm-control/tree/master/storm_control/sc_hardware>`_ for common devices such as cameras, stages, etc. The `software section <http://zhuang.harvard.edu/software.html>`_ of Zhuang's lab website provides a lot of tools not only for acquiring data but also for analyzing it. They even provide some files for 3D printing parts to improve commercial microscopes. It is, overall, a very good example on how a lab can move to open source.

Instrumental - Mabuchi Lab
^^^^^^^^^^^^^^^^^^^^^^^^^^
`Instrumental <http://instrumental-lib.readthedocs.io/en/stable/>`_ is a package aimed at simplifying the automatization of experiments. According to their own description:

   Instrumental’s goal is to make common tasks simple to perform, while still providing the flexibility to perform complex tasks with relative ease.

`The code <https://github.com/mabuchilab/Instrumental>`_ is a great place to look for drivers and understand how different things can be achieved; for example, they have built a low-level `network driver <https://github.com/mabuchilab/Instrumental/blob/master/instrumental/drivers/remote.py>`_ that allows triggering actions on devices remotely. They also have developed drivers and good examples on which to base further developments.

Odemis - Delmic
^^^^^^^^^^^^^^^
Odemis stands for `Open Delmic Microscopy Software <https://github.com/delmic/odemis>`_. `Delmic <http://www.delmic.com/>`_ is a company that develops hardware for correlative electron and optical microscopy and has made the software freely available. It is a great place to see how a professional program looks like. It is very well designed and has a lot of functionality that is hard to observe in other programs. For example, the backend and the frontend are detached, therefore it is very flexible for implementing extensions. Odemis is a very good example of how a company can distribute its software openly, while maintaining its focus on their core business: hardware development.

Qudi - University of Ulm
^^^^^^^^^^^^^^^^^^^^^^^^
`Qudi <https://github.com/Ulm-IQO/qudi>`_ started small and grew over the years to a complete package for controlling devices. Their own description says:

   Qudi is a suite of tools for operating multi-instrument and multi-computer laboratory experiments. Originally built around a confocal fluorescence microscope experiments, it has grown to be a generally applicable framework for controlling experiments.

The code is fairly complex to follow, but they have many `GUI resources <https://github.com/Ulm-IQO/qudi/tree/master/gui>`_ to kickstart your own development; both compiled python and designer files are available.

Lantz
^^^^^
We have discussed about `Lantz <http://lantz.readthedocs.io/en/0.3/>`_ in `the past <{filename}../python/introducing_lantz.rst>`__. It is a development similar to Instrumental, also brought to life by researchers; its main difference is that it is a collaborative effort and therefore it is not directly associated with a single university. On the downside, the development has been stalled for the last several months.

One of the main advantages of Lantz is that it documents very clearly how to `write your own drivers <http://lantz.readthedocs.io/en/0.3/tutorial/building.html>`_ and the ``Features`` and ``Actions`` are incredibly handy when developing. If the efforts of Lantz and Instrumental would be combined, the project would take a very interesting turn.

Micro Manager
^^^^^^^^^^^^^
In the microscopy world, you can never forget about `Micro Manager <https://www.micro-manager.org/wiki/Micro-Manager_User%27s_Guide>`_. It is a complete microsopy software available online and it is a totally open source software. The documentation is very complete, including `video tutorials <https://www.youtube.com/channel/UCdEVRfRFicVCGnS7840O_rQ>`_. Micro Manager, however, is very complex and therefore it is most suitable for plug-and-play. It is the kind of software that you install and it either works or it doesn't. Expanding it or learning from its code is very involved and therefore requires a lot of expertise in this particular program.

Other Software
^^^^^^^^^^^^^^
These are a mix of resources that may be worth checking, depending on your applications.

* `OpenCV <http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html>`_: *supports a lot of algorithms related to Computer Vision and Machine Learning and it is expanding day-by-day.*
* `AndorSDK2 <http://pythonhosted.org/andor/>`_: *Object-oriented, high-level interface for Andor cameras.*
* `PyQtGraph <http://www.pyqtgraph.org/>`_: *Scientific Graphics and GUI Library for Python.*
* `Smart Scan <https://www.single-molecule.nl/smart-scan/>`_: *control confocal microscopes and automate repetitive tasks.*
* `PyMeasure <http://pymeasure.readthedocs.io/en/latest/index.html>`_: *makes scientific measurements easy to set up and run.*
* `PyQLab <https://github.com/BBN-Q/PyQLab>`_: *A python library for instrument control and superconducting QIP experiments.*


Header photo by `Samuel Zeller <https://unsplash.com/photos/2BHDrWzyCto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`_ on Unsplash