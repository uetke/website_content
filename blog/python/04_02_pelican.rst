Ultimate Guide to Python Pelican: Customizing
=============================================

:status: draft
:date: 2018-03-19
:author: Aquiles Carattino
:subtitle: Learn how to generate static websites with Pelican
:header: {attach}storage.jpg
:tags: HDF5, Python, Data, Data Storage, h5py
:og_description: First part of the series on how to develop a website with Pelican

In the previous tutorial you have learned how to start a pelican website with the default configuration and how to deploy it to a Github pages repository. In this tutorial you are going to learn how to customize your website by adding a new template and plugins. You will also learn how you can develop your own themes and plugins to customize your experience even further.

All the code of this tutorial is available in `Github <https://github.com/uetke/pelican-tutorial/tree/0.2>`_.

1. Set-up

   a. Installation
   b. Local build
   c. Adding content
   d. Deploy to a server

2. Custom settings (This tutorial)

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

Adding a template
-----------------
Pelican offers a variety of ready-made templates that can be found at `www.pelicanthemes.com/ <http://www.pelicanthemes.com/>`_ and in `this repository <https://github.com/getpelican/pelican-themes>`_. Working with themes in Pelican is not super straightforward, mainly because of the design of the configuration files of Pelican. You can select the template that you want, but I will be using `pelican-alchemy <https://github.com/nairobilug/pelican-alchemy>`_.

The Pelican documentation suggests to use a command line tool called ``pelican-themes`` to install and remove themes from your website. Even if simple, it is not a sustainable approach for what we want to achieve later on with automatic deploying. The best idea would be to download the theme you want and copy it to your *website* folder. Sadly, the themes are all together in the same repository, meaning that you either download them all or don't download any at all. Go to the root of your project, where you see the *venv*, *output* and *website* folders and run the following:

.. code-block:: bash

    $ git clone --recursive https://github.com/getpelican/pelican-themes.git

Which will create a folder called *pelican-themes* with all the available themes, also those that are submodules (i.e. external repositories). Arm yourself with a lot of patience, because you are downloading a lot of themes at once. If you want to shorten the time, you can grab only **alchemy**:

.. code-block:: bash

    $ git clone https://github.com/nairobilug/pelican-alchemy.git

Now, we should copy the theme we want into our website folder. If you downloaded all the themes, you can do:

.. code-block:: bash

    $ mkdir website/themes
    $ cp -r pelican-themes/pelican-alchemy/alchemy/ website/themes/

If you downloaded only alchemy:

.. code-block:: bash

    $ mkdir website/themes
    $ cp -r pelican-alchemy/alchemy/ website/themes/

Once you have copied the theme, you have to update **pelicanconf.py** with the following:

.. code-block:: python

    THEME = 'themes/alchemy'

Build the website again and you should see an output that looks like this:

.. image:: {attach}pelican_screen_04.jpg
    :alt: Beautiful Bootstrap Pelican website

One of the main disadvantages of Pelican themes is that they are not self documenting nor use a common set of parameters. Therefore you have to search for the documentation of each theme in order to understand how to set it up. For example, this is whay alchemy provides:

    SITESUBTITLE: Subtitle that appears in the header.
    SITEIMAGE: Image that appears in the header.
    DESCRIPTION: Index HTML head <meta> description.
    LINKS: A list of tuples (Title, URL) for menu links.
    ICONS: A list of tuples (Icon, URL) for icon links.
    PYGMENTS_STYLE: Built-in Pygments style for syntax highlighting.
    HIDE_AUTHORS: Hide the author(s) of an article - useful for single author sites.
    RFG_FAVICONS: Use a realfavicongenerator package.

    DISQUS_SITENAME
    GAUGES
    GOOGLE_ANALYTICS
    PIWIK_URL
    PIWIK_SITE_ID

If you open again **pelicanconf.py**, you can add or modify any of the properties. For example, you can add:

.. code-block:: python

    SITESUBTITLE = "Subtitle For My Test Website"

And you will see that a subtitle appears on your website. You should also note that the links that appear just under your header can be changed from the config file. Look for the ``LINKS`` property and change them as you see fit.

Since later on in this tutorial we are going to cover how to build your own templates, we are not going to the details of each property. Once you learn how to write your theme, you will be able to read and understand templates made by others. You will also realize that quite often there are options that were not properly documented, but that you can still use.

The idea of copying the theme into the folder may or may not be a good idea depending on every user case. For example, by copying the contents of the theme folder, if the developer releases an update, our website will not receive it. On the other hand, if we modify the theme, we will need to keep track of the changes in order not to loose them if an upgrade is released.

There is another scenario, where you automate the building process and you want to minimize the amount of dependencies, as we are going to see later in this series of articles. If you are always going to build in your local machine and upload the content to a server, then you can clone the repository somewhere, just as we did earlier. In your **pelicanconf.py** instead of using a relative ``themes/alchemy``, you would include the full path:

.. code-block:: python

    THEME = '/path/to/theme/pelican-alchemy/alchemy'

And you can handle your theme as any other git repository, pulling updates when you want and rebuilding your site. If you want to publish to github pages, you can do it in the same way as we have seen last time.

Adding a plugin
---------------
Plugins are tools that allow us to change how the website is generated, either by adding new content, veryfing the integrity of it, etc. They allow us to write articles in different formats, not only reStructured Text and Markdown. There are plugins for computing, for example, how long is it going to take to read an articles based on the length. However, many of the plugins need to alter the theme, and we don't want that yet.

That is why we are going to work with a plugin that generates an extra output, the sitemap of the website. Installing plugins works in the same way as with themes. We need to download the plugin repository. Go again to the root of your project and run the following command:

.. code-block:: bash

    $ git clone --recursive https://github.com/getpelican/pelican-plugins

As with themes, you can include plugins by referencing to their location and the advantages and drawbacks are the same. I recommend copying the plugin you are interested in into your website folder, in order to keep things tidy.

.. code-block:: bash

    $ mkdir website/plugins
    $ cp -r pelican-plugins/sitemap/ website/plugins/

And again, as with the theme, you can set the plugins you want to use in your **pelicanconf.py**:

.. code-block:: python

    PLUGIN_PATHS = ['plugins']
    PLUGINS = ['sitemap']

The variable ``PLUGIN_PATHS`` holds the directories where pelican can find plugins. Since we are copying the plugin into the website folder, we just type plugins. But you can also use absolute or relative paths. For example:

.. code-block:: python

    PLUGIN_PATHS = ['plugins', '/path/to/plugins/pelican-plugins']

The second variable lists all the plugins that we want to use, in our case it is only the **sitemap**. If you run again pelican to build your website, the following should happen:

.. code-block:: bash

    $ pelican
    WARNING: sitemap plugin: SITEMAP['format'] must be 'txt' or 'xml'
    WARNING: sitemap plugin: Setting SITEMAP['format'] on `xml'
    Done: Processed 3 articles, 0 drafts, 0 pages and 0 hidden pages in 0.25 seconds.

The program runs, but with some warnings. Let's first check in our output folder, you will see that you have a new file called **sitemap.xml**. If you open it, you will see that it contains all the pages of your website. Sitemaps are useful to let search engines know where are your pages and how often do they update. If you refer to the `plugin documentation <https://github.com/getpelican/pelican-plugins/tree/master/sitemap>`_ you see that, even if you are not required, you can specify a variable called ``SITEMAP`` to store the configuration. For example, you can add the following to **pelicanconf.py**

.. code-block:: python

    SITEMAP = {'format': 'xml',}

And if you re-build your website, you shall see that there are no more warnings.

Caution when using plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~
Plugins are a great way of extending the behavior of a package without altering the core code. However, Pelican plugins have a broad range of qualities, both in their implementation and in their documentation. Therefore, using plugins can become a challenge. The ecosystem is not very mature and the quality is not optimal. If you are used to the options you find in Wordpress or Jekyll, you will notice a huge gap when comparing with Pelican.

Some plugins are very outdated and support older versions of Python but not Python 3, for example. Some use extra dependencies which may be a challenge to install in some platforms. In any case, you can use other's plugins as examples for your own development. As we are going to see in the next tutorial. Always keep a critial mindset when you think about implementing a plugin for your website and be ready to invest a bit of time debugging.

Conclusions
-----------
In this tutorial you have learnt how to change the look of your website by adding a theme. We have seen different ways of getting a theme and installing it to your website. Themes are a great way of personalizing your website and make it a more unique place on the internet. However, some themes are not straightforward to install and require some tweaking.

We have also seen that you can use plugins to
