Optical Tweezers
================

:slug: projects/optical-tweezers
:subtitle: Monitoring in real-time the movement of nano objects
:keywords: Optical, Tweezers, Trap, QPD, Imaging

.. image:: {attach}UUTrap_Screenshot.png
   :alt: Screen capture of an optical tweezer in action

Optical tweezers are becoming a ubiquitous tool in many research labs. Optical tweezers, sometimes also referred to as *optical traps*, are based on a tightly focused laser that is able to exert a force on small objects such as metallic nanoparticles or dielectrics. In the end, the principle under which they work is the same principle responsible for attracting a piece of paper to the tip of a plastic bar.

Most confocal microscopes already have all the needed elements for building an optical tweezer: a tightly focused laser beam and an imaging system. However, measuring the force applied to the particles normally is done by monitoring very small fluctuations in the particle position. Since these displacements can be very small and fast, it is ideal to employ a Quadrant Photodiode (QPD). These devices are photodiodes split into four quadrants and provide three different outputs: the difference between the top and bottom halves, the difference between left and right and the total intensity.

When manipulating an optical tweezer, it is therefore fundamental to monitor at least three signals. Studying the variance of the signal is a good strategy to check if a particle is already trapped while calculating the power spectrum allows calculating the force exerted by the trap. At Uetke we have developed a solution for the `University of Utrecht <http://www.nanolinx.nl/index.php/research/nanoelectrophotonics/>`_ that employs a National Instruments card to monitor those signals. The results are displayed in real time and can be acquired with very high temporal accuracy.

The code can be found at `Github <https://github.com/uetke/UUTrap>`_.