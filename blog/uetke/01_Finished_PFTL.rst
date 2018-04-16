First Edition of Python for the Lab Was a Success
=================================================

:date: 2018-04-16
:author: Aquiles Carattino
:subtitle: The group of Michel Orrit at Leiden University was the first to participate
:header: {attach}class_room.jpg
:tags: Course, Workshop, Leiden University, Instrumentation, Python, Michel Orrit, Lab
:og_description: Michel Orrit's group was the first to participate in the Python For The Lab Workshop

The group of `Michel Orrit <http://single-molecule.nl/>`_ at Leiden University was the first one to participate in the `Python For The Lab workshop <https://uetke.com/courses/pythonlab/>`_. In total, seven students gathered for three full days of coding and development. We discussed design principles, the basics of instrumentation and built a small experiment to measure the current that passes through a diode as a function of the voltage applied to it. The workshop also included the creation of a Graphical User Interface (GUI) to control the measurement.

On the first day, we have covered the very basics of Python in order to break the ice with the language. Participants were acquainted with lists, dictionaries, and loops. In the afternoon, they received a small DAQ card and some electronic elements in order to build the experiment. Together, we established communication with the DAQ through the serial port and varied the voltage applied to an LED. The most important message from the day was the importance of creating classes to make reusable and easy to share code.

On the second day of the course we discussed the meanings of the Model-View-Controller design pattern for lab applications. Having a clear separation between different elements of the code is fundamental to make robust programs that can be maintained in the long term and by different developers. Participants learned how to build a model for the DAQ device and a model for the experiment. With this experience, the day ended with the creation of a simple user interface that allowed to trigger a measurement.

The third and last day was focused on the development of a graphical user interface (GUI) around the experiment model. Participants have learned how to work with different threads in order to achieve a smooth behavior of the interface. They have seen how to embed a plot that refreshes automatically while the experiment is running. They have also seen some general patterns in user interface development and learned how to take input from the users of the software.

Overall, the first edition of Python for the Lab has been a success. It has been an intensive week, but with lots of sharing and learning.

To learn more about the workshop, check the `Workshop Page <https://uetke.com/courses/pythonlab/>`_ or `contact us <https://www.uetke.com/contact/>`_.

Header photo by `Mikael Kristenson <https://unsplash.com/photos/3aVlWP-7bg8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`_ on Unsplash