Should Labs Move to Open Source?
================================

:tags: Open Source
:header: {attach}sorry_we_are_closed.jpg
:date: 2018-02-18
:og_description: Why and how can labs move their projects to Open Source? The tools are there; it is interest that is missing.

We can agree that researchers exchange published papers as a currency, and its value is the number of citations each has. Accessing conferences, faculty positions and grants is to a great extent achieved on the basis of researchers' success history. However, publishing software is not counted towards a scientist's productivity, regardless of how many scientists are benefiting from it. Therefore there is no official incentive in publishing software and much less as open source; therefore it has to be a policy established from top to bottom, from management to Ph.D. candidates.

It is fair therefore to ask ourselves how can we benefit from publishing software as open source. The answer is not at all clear and aims at the long term more than to quick solutions. I think that publishing software as open source is the fastest way of creating a community (even if it can be small) around a topic of interest. For example, you can publish software for analyzing a very specific type of data; someone may find your code useful and add an extra option that perhaps you didn't think of, or you didn't have time to include. And, as simple as that a collaboration was born.

It is a collaboration that doesn't have a direct impact on the researcher's output; it is not a citation and it is not a new paper. However, this simple interaction has improved the data analysis for whoever else is struggling with the same kind of experiments. This is the romantic option of what could happen after publishing software. More often than not, it will happen the same as what happens with the majority of papers: it goes unnoticed.

When controlling setups, sharing code is crucial to avoid overlapping of efforts. If anybody has ever tried to interface with complex devices such as a Hamamatsu camera, the first thing you notice is a complete absence of documentation regarding how to use their API. Fortunately, a quick look around shows that members of `Zhuang Lab <http://zhuang.harvard.edu/>`_ have developed a `Python wrapper for the cameras <https://github.com/ZhuangLab>`_. You can just use their code in your own project, thanking them when appropriate and you have saved weeks of backs and forts with the technical support.

The tools for switching to open source
**************************************
Nowadays there is a standard tool for sharing code online: `Github.com <https://github.com>`_. Github is a web interface for servers running Git version control. It does not only allow you to publish software, it also allows you to generate wiki pages, track issues, changes to the code, generate documentation pages, and many more options. Just by putting your code into GitHub, you make it accessible and searchable. It is very easy for anybody else to grab your code, improve it and share the changes with you.

Everything happens in a transparent way and therefore you know who has *forked* your code and is working on it. You can see what they are doing, engage in discussions and suggest improvements. Everybody can see the discussions, the issues, propose solutions or ask for features. The advantage is that everything is achieved through a clean and clear interface, where managing repositories are done relatively painless. There are no limits to the number of repositories you can have, nor to the size of the code you are hosting. Very big projects such as `Python <https://github.com/python>`_ are hosted on Github but also very small ones like the software I use for tracking `the temperature of my house <https://github.com/aquilesC/trackmytemp>`_.

There are other tools that allow you to publish code online; however, Github is the one that has the largest community of people working on projects. Of course, if your work belongs to a specific niche, that revolves around other platforms you should seriously consider them.

Policies for a Successful Open Source Group
*******************************************
The key to having a successful open source project within a lab or institute is to establish clear rules regarding what to do, how to do it and when. A lot of people think that for publishing software to GitHub it has to be spotless, ready to use and incredibly well documented. This means that it will never end up in the open source community because it will never be completely ready, it will always have some bugs and there is always going to be something to document better.

Therefore it is never too early to go Open Source; if you do it since the beginning, you will always have it in mind when documenting, developing, etc. Therefore a smart first rule would be to always do version control on a public repository. But then, people have to keep using the repository, and therefore the second rule should be that at most every week you should commit all the changes to the public repository. When overwhelmed by work in the lab, writing papers and preparing the exercises for a class, it is very common to neglect the publishing of the updates of the code.

It happens that the normal attitude is to publish when you are completely sure of what you are doing; don't be so self-critic. Publishing the changes to your code often will help you with organizing yourself plus you open the door to someone else catching a bug in your code. If you are collaborating with members of your group or elsewhere, you should also establish rules regarding how to propose changes and improve the code.

.. image:: {attach}laptop-with-memory-stick.jpg
   :alt: Laptop on table with a usb memory stick

If you are working with Github, you can start a new project, which will have its own page; something like  ``github.com/project``. You will also need to determine who is going to be able to write to the repository; if there is a leader, or if anybody can make changes. The latter, bear in mind, poses a risk especially if developers are not used to working in teams since bugs can be introduced, ruining everybody's work. Github has the possibility of forking the code, and therefore everybody can develop in their own repository, while changes are merged into the main project only when approved by the project leader.

Each project and each group may have different workflows, but if you have clear rules since the beginning, you will avoid a lot of confusion later on. The use of branches, and what each branch means is of utmost importance. Keep the master branch always tested and working; add a development branch in which you are going to test new features. Try to keep it tidy; if you have thousands of branches it is going to be very hard which one you should check in order to test a new functionality.

Using the merge requests in Github allows the project leader to comment on code before adding it to the main repository; if the documentation is not correct, or the common style is not followed, etc. You can use the merge requests as an opportunity to teach the members of the team how to work together. You can use the issues pages of the project to generate discussions over topics (not necessarily a bug) and keep them searchable and open. Maybe something was already discussed and solved, or there was agreement, or it is still something open; in any case, the users can find it.

How to Maintain the Secrecy
***************************
It is a common concern for researchers how not to make available software that could help the competition in publishing faster. It may not be just because of the software, it may be that the software is a big hint of what the group is doing or where interesting results are to be found. Github offers `pro accounts <https://github.com/pricing>`_ which include private repositories; they are free for students. `Bitbucket <https://bitbucket.org/product/pricing?tab=host-in-the-cloud>`_ has also interesting options, including free for small teams. Finally, you can opt for a self-installation of `Gitlab <https://about.gitlab.com/>`_, perhaps in your institute servers.

You can keep your repository out from public eyes until your paper is ready and submitted, then you can switch from private to public. Remember that the temptation of keeping it private is big, but you should overcome the inertia and at some point make it accessible. It can also happen that when you change from one lab to another your access rights to a repository are revoked and you lose access to your previous work, not only to your own code but also to the improvements that people do to your own work.

Learn to Use Git Repositories
*****************************
Git is a very complex tool that has a lot of different options. It is useful not only for code, but it can help you in tracking changes while you write a paper or prepare a presentation, for example. There are so many different options, servers, terminology that it can quickly become overwhelming for someone who is starting with the tool.

At Uetke we have developed `a course especially aimed at scientists who want to work with Git <https://uetke.com/courses/gitscience/>`_. The course focuses on what a researcher needs for working in a team, what are the most effective rules for a group. Moreover, it shows different services that may be encountered in labs, including Github, Bitbucket, and Gitlab. It is a realistic 2-day course that will give you enough insight to start working with repositories right away. We will show you how to deal with branches, merge requests and, importantly, we will show you how to build amazing documentation directly from Python code.

It is useful both for lab managers who can learn how to organize the group's work, but also for whoever is willing to learn how to use the tool. The course can be arranged for a closed group or you can join one of the groups at our own location. If you are interested, just check `the course <https://uetke.com/courses/gitscience/>`_, or `drop us a line <https://www.uetke.com/contact>`_ if you have any special requests or suggestions.

Photos by `Tim Mossholder <https://unsplash.com/@timmossholder>`_ and `Brina Blum <https://unsplash.com/@brina_blum>`_ on Unsplash