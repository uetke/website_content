Ultimate Guide to Python Pelican: Setting Up
============================================

:status: draft
:date: 2018-03-19
:author: Aquiles Carattino
:subtitle: Learn how to generate static websites with Pelican
:header: {attach}storage.jpg
:tags: HDF5, Python, Data, Data Storage, h5py
:og_description: First part of the series on how to develop a website with Pelican

Pelican is a great program to generate static websites, i.e. websites that don't need a database to run and in which all the logic is computed at the client side. One of the advantages of static websites is that they are very secure, because there is nothing to hack into. The other advantage is that they are super fast and require very little from the server on which they run. Github pages, for example, allow you to host a static website for free. The cheapest options on many servers are normally more than adequate for websites with more than tens of thousands of visits per day.

On the other hand, the disadvantage of static websites is that there is no user or admin interaction. If you are used to Wordpress, you know that you can install plugins from a common interface, you can grant some users writing or publishing permissions, etc. Moreover, you can let your users leave comments in selected posts or to contact you through a form. In this guide you will see how to develop a workflow that will allow you to quickly deploy static websites generated with Pelican. This is the general structure of the tutorial.

In order to complete the tutorial, you should have a basic knowledge of Git. If it is not the case, you can read the `Hello World Tutorial <https://guides.github.com/activities/hello-world/>`_ that will guide you through some fundamentals and the `15 minute guide to Git <https://try.github.io>`_ which helps you to understand some of the command line options available.

All the code of this tutorial is available in `Github <https://github.com/uetke/pelican-tutorial/tree/0.1>`_

1. Set-up (this tutorial)

   a. Installation
   b. Local build
   c. Adding content
   d. Deploy to a server

2. Custom settings

   a. Adding a template
   b. Adding a plugin
   c. Creating a template
   d. Creating a plugin

3. Version control

   a. Host the code in Github
   b. Use Travis to automate the build
   c. Use webhooks to build on the server

4. Adding comments

   a. Setting up Staticman
   c. Update the template
   b. Render comments


Setting up
----------
The first step in every successful Python endeavor is to `create a virtual environment <https://www.pythonforthelab.com/python/03_virtual_environment/>`_ to hold all the packages and settings and to avoid collisions with the Operating System. Moreover, it will allow you to quickly obtain the list of installed packages that is going to become crucial later on.

Start by creating a folder for your project, for example **PelicanProject** and move into it. We can start a virtual environment for our project with the following command:

.. code-block:: bash

    virtualenv venv -p python3

You are free to choose the version of Python that you prefer. If you have doubts regarding how to use the virtual environment, you can check our `quick introduction <https://www.pythonforthelab.com/python/03_virtual_environment/>`_. And activate it:

.. code-block:: bash

    source venv/bin/activate

**Windows users**, please refer to the quick introduction linked above in order to adapt the commands to your operating system.

We can check that we are working inside the virtual environment by looking at the ``(venv)`` prepended to the command line. Once you are there, you just need to install pelican:

.. code-block:: bash

    pip install pelican

You will notice that pelican comes with a lot of dependencies. If you type:

.. code-block:: bash

    pip freeze

You will see all the packages that were installed. Now it is time to create your website. Pelican comes with a command line tool to bootstrap the process. Type into the terminal:

.. code-block:: bash

    pelican-quickstart

Which will guide you through the process of creating the basics of a Pelican website. If you have a virtual environment folder, it is wise to create the website not at the root, but within a new folder, in order to simplify the version control later on. The options should look like this:

.. code-block:: bash

    > Where do you want to create your new web site? [.] website
    > What will be the title of this web site? My Test Website
    > Who will be the author of this web site? Aquiles Carattino
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) Y
    > How many articles per page do you want? [10]
    > What is your time zone? [Europe/Paris]
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) n
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y

The options are quite straightforward and you can change them later on. If you create a Fabfile/Makefile, it will ask you several questions regarding where do you want to publish your website, allowing you to streamline the process. However, we are going to develop a very robust process later on and we don't really need this functionality at this stage.

Move into the *website* folder and run pelican:

.. code-block:: bash

    $ pelican
    WARNING: No valid files found in content.
    Done: Processed 0 articles, 0 drafts, 0 pages and 0 hidden pages in 0.07 seconds.

If you see that message, it is great news. Now you have a static website, with no content though. You should not that the *output* folder is now populated with a bunch of html files and folders. That is your website! If you open any of the files directly with your browser, you will notice that they look very bad. Open **index.html** and it will look something like this:

.. image:: {attach}pelican_screen_01.jpg
    :alt: Screenshot of a bad Pelican website

The main reason behind this is that the website is using absolute instead of relative paths. If you explore the code of the file, you will notice a line like this:

.. code-block:: html

    <link rel="stylesheet" href="/theme/css/main.css" />

This is telling your browser to look for a file in the root of your computer, but it is obviously there. There are two way of solving this. One is to change the configuration file of Pelican in order to use relative paths instead of absolute ones. The other is to run a local webserver in order to interpret locations relative to the website and not to the computer.

First, let's try changing the pelican configuration file. You should see in your directory that you have a **pelicanconf.py** file. If you open it, you will see that the options that you were asked during the quick start process are there. All the way to the end, you will find an option regarding relative urls. Just be sure it is set to true:

.. code-block:: python

    RELATIVE_URLS = True

Rebuild your website by running ``pelican`` on your command line and re-open the **index.html** file. It should look like this now:

.. image:: {attach}pelican_screen_02.jpg
    :alt: Proper rendering of a Pelican website

And if you explore the code of the file, you will see the following line:

.. code-block:: html

    <link rel="stylesheet" href="./theme/css/main.css" />

The change is very subtly in this case. There is ``.`` added at the beginning of the path. This is all it takes to transform an absolute path into a relative path. The other option is to run a simple server in order to have a situation closer to what you would find once you publish your website. Move to the *output* folder and run the following command:

.. code-block:: bash

    python -m pelican.server

And now point your browser to `http://localhost:8000/ <http://localhost:8000/>`_. You should see your website correctly displayed. If you want to really test it, what you should do is to set the ``RELATIVE_URLS`` back to ``False``, build again the website with ``pelican`` and check that it is still looking great, even if paths point to the root.

Adding Content
--------------
Having an empty website is a bit dull. Adding content to a Pelican website is achieved through writing text files into the *content* directory. By default Pelican accepts articles written in `Restructured Text <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ which is the same markup language used to document packages in Python. It really simplifies the task of writing html code.

Create an empty file called **beginning.rst** and add the following to it:

.. code-block:: rst

    This is the first article
    =========================

    Welcome to the first article in the blog

If you try to build your website again, it will give you an error:

.. code-block:: bash

    $ pelican
    ERROR: Skipping ./beginning.rst: could not find information about 'date'
    Done: Processed 0 articles, 0 drafts, 0 pages and 0 hidden pages in 0.09 seconds.

You are seeing the error because the only way that pelican has to order your articles is through their dates. If you don't specify one, it will not know which article was written before and which one was written later. There are, again, two ways of solving it. The first would be to add a default date to your articles, based on the last modified time of them. Edit the **pelicanconf.py** and add the following:

.. code-block:: python

    DEFAULT_DATE = 'fs'

If you build the website again, you will see the following:

.. code-block:: bash

    $ pelican
    Done: Processed 1 article, 0 drafts, 0 pages and 0 hidden pages in 0.12 seconds.

Refresh your website, and you will see your article. You can also try adding a more sophisticated entry. Go to the `Github repository <https://raw.githubusercontent.com/uetke/pelican-tutorial/master/content/use_decorators.rst>`_ to download a full article regarding how to use decorators. Copy the contents into a file called **use_decorators.rst**. You can build again the website and see the changes. The example article uses already several options of the Restructured Text Format, such as including code.

Changing the Headers
~~~~~~~~~~~~~~~~~~~~
A very useful option in Pelican is to change the headers of the article in order to specify the publishing date, the author, the category, etc. Open again the file **beginning.rst** and update it:

.. code-block:: rst

    This is the first article
    =========================

    :author: Not Me
    :category: Base Category

    Welcome to the first article in the blog

If you rebuild your website, you will see the changes appearing. You will also see that, since you modified the article, it will appear at the beginning of the list of articles. If you want to keep the order of the articles, it is better to add a date parameter, for example:

.. code-block:: rst

    :date: 2018-05-01 15:15

My personal suggestion is, remove the ``DEFAULT_DATE = 'fs'`` option from the config file and always include an explicit date to your articles. It is very common that you need to update the links in an older article, or add a note, etc, and you don't want it to pop up at the beginning of your list.

Using Markdown
~~~~~~~~~~~~~~
With Pelican you are not restricted to using Restructured Text, you can also use Markdown. The only thing needed to make it work is to install it:

.. code-block:: bash

    pip install markdown

If you create a file with an extension like ``.md``, ``.markdown``, ``.mkd``, or ``.mdown`` it will be parsed automatically. You can test it by creating a new file called **testing_markdown.md** and adding some contents to it, for example:

.. code-block:: md

    title: Testing Markdown

    This is a test of a markdown article, with some code:

    ```python
    print('This is Python')
    ```

    # With some title
    This is a new section

I personally prefer restructured text, because it allows me to to quickly develop documentation for my Python projects and re-use some of its contents in blog articles. However, markdown is very popular in other contexts, for example for writing readme files on Github and with other static generators such as Jekyll, not written in Python.

Deploy to a web server
----------------------
At this point you already have a website, but it is running only on your computer. It is time to deploy it somewhere to make it public. The easiest solution at this stage is to use `Github Pages <https://pages.github.com/>`_, which allows you to host static websites for free under a domain such as *username.github.io*. The only thing you will need to do is to submit the output folder into a special repository and you are ready to go.

The first step is to create a new repository, and call it ``username.github.io``, where ``username`` should be your own Github username. Now it is a good time to structure your project in the proper way to avoid nesting of repositories. In the command line, move one level up, so now you are in the folder that contains both *venv* and *website*. You can run

.. code-block:: bash

    $ pelican website/content/ -o output -s website/pelicanconf.py
    Done: Processed 3 articles, 0 drafts, 0 pages and 0 hidden pages in 0.22 seconds.

With this command, you are telling pelican where your content is located, where to output the website and which configuration file to use. Up to now, you pelican was using the default values, generated with the ``quickstart``, but we need to move pass it. Move into the *output* folder and type the following commands:

.. code-block:: bash
    :hl_lines: 2

    $ git init
    $ git remote add origin git@github.com:[username]/[username].github.io.git
    $ git add .
    $ git commit -m "Initial website commit"
    $ git push -u origin master

If you are having trouble connecting to github with the ssh version (the highlighted line), you can try to do:

.. code-block:: bash

    $ git remote add origin https://github.com/aquilesC/aquilesC.github.io.git

Which should ask for your login credentials when you want to push to the repository. Once the files are uploaded, you can visit https://[username].github.io and see your live website. Pretty cool, isn't it?

.. note:: If you are having trouble seeing the website, you can add ``/index.html`` to the address. Sometimes it takes time for Github to update the page.

Conclusions
-----------
In this tutorial, you have learned how to start a Pelican Project and how to host it into a github pages repository. You can play as much as you want, add more content, try to see how far you arrive. In the next tutorial, we are going to cover how to change the template and add some plugins. We are also going to cover how to develop your own plugins and tweak your template.

If you want, you can check the code of this tutorial at the `repository <https://github.com/uetke/pelican-tutorial/tree/0.1>`_.
