Is it worth for companies to switch to Python?
==============================================

:header: {attach}office_with_chairs.jpg
:subtitle: How can companies better meet their customers demands
:tags: companies, open source, resources
:date: 2018-02-16
:og_description: Companies could start listening to their customers and start providing support for popular languages such as Python

It is a very fair question that has popped up several times while explaining what Uetke is trying to achieve. Is it worth switching to Python when most instrumentation is done with LabView? To address this question, there are several things to consider, such as who is actually building the instrumentation for a particular setup, who is using it and which devices are available.

Setups can be split broadly into two different categories: home built and commercial. Home built setups are those developed within a lab, including not only pieces of hardware but also the software. A piezo stage, an objective, and a detector can be used for building a microscope, but a computer needs to control the different components to make an image. Commercial setups are normally built by companies, providing not only the hardware but also the software in order to deliver functional equipment. A microscope from Zeiss, Nikon, etc. will be shipped together with software to acquire an image.

Labs and corporations are very different in the availability of human resources and therefore on the technologies they choose to employ. A mid-size lab cannot afford a permanent engineer just to develop software, while larger companies can. Normally this means that the software development in the labs will be done by a Ph.D. or Postdoc, using the tools they already know, or the tools already available in the lab. Companies, on the other hand, can have a longer-term view, shaping standard practices and developing ad-hoc tools for their devices.

Traditionally, developing software for a setup was a synonym of National Instruments’ LabView. It is a graphical programming language, in which you can quickly build user interfaces by dragging boxes and making connections on a screen. Many other companies provide drivers for it and therefore if you want, for example, to acquire an image from a camera, there was already code written in LabView that you could use as an example. I can understand the success it had twenty years ago when computer literacy was much lower than what it is today: it has relatively low entry barrier and myriads of devices supporting it.

.. image:: {attach}team_training.jpg

Nowadays it is not safe to assume that all scientists are proficient in programming languages, but it is very fair to assume that computer literacy is much higher than twenty years ago. This means that it is much more likely to find someone comfortable writing a for loop than dragging cable connections on a computer screen. And partly this happened thanks to some languages that emerged as standards in different fields, with some common factors: They are not compiled, they are cross-platform, easy to read and with a large community around. I can quickly think of three examples: Matlab, Python, and R.

Focusing on Python, you will see that it possesses all the mentioned qualities plus it is open source. Python is a great tool for data analysis, there are already several packages with tools for biologists, image analysis, astronomy, etc. There are packages for plotting, for saving large amounts of data, for manipulating units. This means that the community of scientists is already there, but what they are just now starting to realize is that controlling setups can also be achieved with the same language they use for data analysis.

And here is where companies can have a great say in the future of Python for instrumentation. If you are providing a tool for research, you should also provide enough openness for scientists to improve upon your tool. If I have an idea that cannot be developed simply because your software doesn’t allow me to, I will either desist, switch companies or spend months working around the problem. If you provide clean documentation and examples, I won’t even bother your technical support.

So far companies have been rooting for National Instruments, even if they have no interests with them (or at least they don’t declare any interest). On the other hand, scientists are rooting for open source, transparency and lowering costs. Companies providing tools for research can greatly benefit from the synergy of a large community built around some common practices. It is much more likely to find a scientist who knows how to program in Python than with LabView, so why forcing them otherwise?

The switch to Python is happening, whether companies will be proactive or reactive is something to see in the coming years. I honestly believe that those who anticipate the change will be the great winners. Companies that can nurture their communities can innovate faster and more efficiently.

If you are willing to learn how to control your setup with Python, check our `Courses page </courses>`_.