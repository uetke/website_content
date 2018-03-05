Network Control
===============

:keywords: flask, network, raspberry pi, beaglebone
:subtitle: Control any device through the network
:slug: projects/network-control
:header: {attach}beaglebone-black-front.jpg

Small devices such as a **Raspberry Pi** or a **Beaglebone** come with native network capabilities, USB ports, and basic DAQ. Even if it is possible to connect a device to the network through one of these small computers, it is still not possible to control the device remotely. At Uetke we have developed a server that with a simple API is able to relay commands to any connected device.

In the server computer (for example a **Raspberry Pi** or **Beaglebone**) you only need to run a script:

.. code-block:: python

   from instserver.server import InstServer
   from instserver.dummyDevice import dummyDevice

   # First instantiate the device
   dev = dummyDevice()

   # Now is time for the server:
   server = InstServer(__name__)
   server.add_device(dev,'dev')
   server.run(debug=True)


From the client, you can communicate with the device by running:

.. code-block:: python

   from instserver.client import InstClient
   # First instantiate the client with the IP address and port of the server
   c = InstClient('http://127.0.0.1:5000')
   # Let's print a list of the available devices and methods on the server
   print(c.listdevices())

The server was built on Flask and thus has a minimal footprint on resources. It was thought as a relay of commands that are received from the network connection to the specified device. If you need something reliable for having your device running every time that your computer starts, you can see how to configure `Gunicorn and Nginx <https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04>`_.

Controlling devices through the network is very handy, especially when you need to keep older computers around in order to work with legacy hardware. Using small computers such as a Raspberry Pi enables to hook any device to the network for a very reasonable amount of money. The options are limitless.

Check the code of the project on our `Github page <https://github.com/uetke/UUServer>`_.