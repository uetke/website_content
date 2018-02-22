Camera Acquisition
==================

:keywords: Camera, Framerate, Fast, Parallel, Tracking
:subtitle: Fast frame rates for tracking and monitoring
:slug: projects/camera-acquisition

Imaging with digital cameras allows scientists to acquire large amounts of data in short periods of time. Ranging from entire cells to tracking of nanoparticles, imaging is a fundamental tool in a broad range of fields, and combined with high frame rates, allows to investigate properties that would have been otherwise averaged out.

NanoCapillary Electrokinetic Tracking (`nanoCET <https://www.ncbi.nlm.nih.gov/labs/articles/27711894/>`_) is a new technique for continuously measuring the electrophoretic mobility of a single colloidal nanoparticle or macromolecule *in-vitro* with millisecond time resolution and high charge sensitivity. `Sanli Faez <http://lab.sanlifaez.com/>`_ has been developing this technique and needed a software for monitoring a camera while streaming the data to disk.

At Uetke we have developed a Python-based GUI that is able to display a live stream from a camera. Moreover, it is capable to save to disk while the acquisition is happening, allowing frame rates in the order of the kilohertz while not overflowing the graphics card. Metadata is automatically saved into each file to allow reproduction of experiments and traceability. Some extra perks include the possibility to track particles *in-vivo*, effectively compressing the data saved to disk, a waterfall widget that plots a 2-D representation of the data, and many other options.

The tracking software developed by **Uetke** is a very good example of the level of complexity that has to be handled by laboratories all around the world. The *MVC* model enables future users of the program to expand its capacities according to changing needs. Adding new cameras, changing the localization algorithm or background correction are only a few lines of code away. Uetke is able to accommodate all the needs of researchers and deliver even beyond expectations.

You can see the code of the project on our `Github page <https://github.com/uetke/UUTrack>`_.