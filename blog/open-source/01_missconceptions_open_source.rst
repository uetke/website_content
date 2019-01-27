Missconceptions Around Open Source Software
===========================================

:tags: Open Source, Open, Software, Packages, Programs, Open Science, Science, Labs
:header: {attach}sorry_we_are_closed.jpg
:date: 2019-01-27
:og_description: What does open-source mean and what can it do for your lab or company
:author: Aquiles Carattino

Last week I gave a talk at Utrecht University in which I presented `the PyNTA package <https://pypi.org/project/pynta/>`_ to an audience of researchers. In the talk, I stressed the fact that PyNTA is free, open source, and is hosted on Github. However, one of the professors was not convinced with what I was saying and made several remarks and ask questions that I believe should be addressed also publicly.

Many of the concerns around open source software are rooted in a lack of understanding of what *open* stands for. The core idea is that anybody who receives an open source program can inspect its code, see what it does, learn from it and perhaps modify it. Bear in mind that I said receives the code and not gets the code. Someone can hire me to develop a program and I deliver the source code of it. In these few sentences, there are different points that are worth stressing.

Open source software doesn't imply that it is publicly available. A lot of open source software is developed under request and can't be downloaded from the internet. A simple example from research institutions are the dozens of scripts created to analyze data. If a colleague ever asks for the script, you can share the source code, but you won't put it online for the rest of the world to download. I know this scenario is a stretch for most of the readers, but being able to see the source code of a program is the exact definition of open source.

The development of open source software is not free. Someone invested time in it and that time is more often than not paid by an organization. For example, the software developed at Uetke is always open source, we always deliver programs that can be used to learn and can be expanded by others. But we don't work for free, we are not a charity either. Therefore, it is possible to build a business around open source software. There is no contradiction between commercial interest and open programs.

Part of the discussion was around the fact that `PythonForTheLab <https://www.pythonforthelab.com>`_ is a ``.com`` and not a ``.org``. The fact that the particular domain is reserved for commercial activities is not in contradiction to the open-source nature of Python. Services built around free tools can be viable businesses. Such is the case of Github, for example, in which the core element, Git, is open source, but the service they provide has many paid features. And this brings us to the next hook, the role of Github for open source programs.

Github was acquired by Microsoft some months ago and many started to speculate what the future of open-source software will be. It is a fact that a lot of publicly available, open-source projects are hosted on Github. However, the owners of the code are not the ones who host it. It has to be remembered that Git is distributed by design. This means that I can bring the code to any other host in just two commands. If Microsoft ever kills the possibility to host open source programs, there will be an exodus to any other provider, such as Gitlab.

Finally, there is this idea that everybody can do whatever they want with open source software. The software is distributed with a license, in which it is clearly specified what can and cannot be done with the received product. Some licenses are very open and allow users to do whatever they want, even re-distribute the code with a different license. Some ask to keep the same license, others forbid to re-distribute the code, etc. Open-source software comes with legal limitations, in much the same way as closed-source software does.

The last point I would like to address is the role companies have on open-source software. A paradigmatic example is that of Pandas. It was developed within a financial company and eventually made open-source. Pandas became a huge success within different communities. What did the company gain by making it open-source? First, it now has a much better product than what it was when closed source. This is due mainly to the fact that now there are hundreds of developers contributing code instead of just one. Secondly, the company made a huge public-relations gain, who knew anything about AQR Capital before?

For startups, free, open-source software has a completely different meaning. Startups are, normally, cash-scarce companies. If your main output is hardware, would you think it is smart to invest an equal amount of money in licenses and in fabrication just to keep your program closed? PyNTA, for example, will become a tool used by a company. The only requisite is that the company releases any modifications to the code under the same license than PyNTA, which gives the users the power to do the same. Other companies can use PyNTA and all together reach new standards for particle tracking analysis.

If PyNTA was to be released under a different license, it would mean getting compatible versions of Qt and PyQt, of the tracking algorithms, of numpy, etc. As a commercial strategy seems very meager. The common argument is that a company loses its *edge* when software is made open source. If the only edge the company has is how it put together a collection of packages and algorithms which are freely available, the business case would be incredibly weak.

The fact that open-source software still generates *controversies* in academic settings is puzzling. One would have imagined that debates over these topics took place a long time ago and that younger generations are encouraged to think about them. However, it seems that there is a big disconnection between the way people say they want to work and how they work in the end. Perhaps there should be a bigger campaign of awareness towards open-source, what it means, what tools are available, and what it entitles.

As I said in the talk last week, and many times in the past, the software can have a very big impact on the careers of researchers, especially young ones. The software can put your name at the top of the minds of other researchers in your field. Moreover, a package used by a community of people is a great addition to the CV of any researcher who plans to transition out of academia. It proves the different values of the person, not only as a programmer.

The moment to open-source your code is not tomorrow, it is today.
