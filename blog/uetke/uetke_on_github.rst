Uetke's website is on Github
============================

:subtitle: This website is built with Python, Pelican, static files, and is available on Github
:date: 2018-02-26
:og_description: Uetke's website is built with Python, Pelican, static files, and is available on Github
:header: {attach}website_analytics.jpg

At Uetke we seek to build simple, clear, modular and extensible codes that can be easily maintained and repurposed by developers other than their creators. Therefore we decided to make all the under-the-hood code freely available for others to read, learn, and improve. The code is hosted on Github in two different repositories: `the content <https://github.com/uetke/website_content>`_  and the `style files <https://github.com/uetke/website>`_. Uetke is built on Pelican, a Python generator of static websites, you can find the plain files in the content and the template and configuration files in the style files.

Some months ago we have realized that the website was lacking speed when loading, and was having some issues with server usage. We were using Divi, an `Elegant Themes <http://www.elegantthemes.com/affiliates/idevaffiliate.php?id=46367>`_ template that was loading several files from other servers and was generating a lot of complex syntax in our pages; moving to a different template was not an easy solution.

Static websites were always an option, but we thought they were suitable for another kind of situations until we decided to give them a try. The obvious advantage of static websites is that the requirements for the web server are minimal; there is no workload on the server side, only serving plain files to users. The downside is that you can't have interaction with your users, such as contact forms without relying on external providers. We could work with that; our priority was to have a fast website and an easy-to-maintain server.

If you look around for a course or instructions on how to build a website with Bootstrap, you will notice a complete absence of examples on how to build templates. In other words, websites have common elements through their pages, and therefore it would make sense to import those elements and not to copy paste and update in a million different files. It felt that all the courses were falling very short for someone who is planning to work in the real-world with plain HTML.

To solve the problem we started to look into Jinja, a Python library for using templates. The beauty of Jinja is that you can use templates for anything, not only websites. If you want to use Jinja for your latex files, for example, you can use it. Jinja is very extensible and complex, therefore reading the documentation carefully is important. In the meantime we've realized that we were using reStructuredText for documenting the software we were developing, therefore it would have made sense to keep everything with the same format, simplifying the copy and paste. That was when Pelican popped up. Pelican is designed as a blogging platform that can transform plain text files into HTML pages. You can use Markdown or reStructuredText for your text files. There are templates based on Jinja and plugins to expand the functionality. Moreover, since it is built on top of common Python libraries, you can write your own plugins and expansions quite easily; you only have to get used to the terminology.

The Final Setup
***************
Since the majority of the website visitors come from The Netherlands, we decided to have our server in Amsterdam. We are currently using `Digital Ocean <https://m.do.co/c/2fbde6232442>`_ with the smallest plan. At only 5€/month, it is a very good deal and it provides enough power to host this and other websites. By the way, if you `click here <https://m.do.co/c/2fbde6232442>`__, you get 10€ credit to start trying it out. We installed and configured Nginx <https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04>`_ and added `SSL encryption <https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04>`_. It takes a while to learn, but it is very gratifying.

To register the domain and hosting the e-mail we have used `Dreamhost <https://www.dreamhost.com/r.cgi?181470/promo/dreamsavings50>`_. We have been their customer for over 10 years and we have never been disappointed. Of course, you can opt to host your website directly with them and it will work more than fine. We just wanted to embark on the adventure of managing our own web server. If you `click here <https://www.dreamhost.com/r.cgi?181470/promo/dreamsavings50>`__ you will get a 50U$ discount when signing up for a yearly plan. At 97U$ (or 47U$ with the discount) for a full year of unlimited hosting, webmail, etc. you won't find a better solution around.

For the website itself, we built a lot of HTML pages that are the ones you see when browsing the site. The courses, the contact us, etc. They are rendered by Pelican when compiling the website, and the main advantage is that we could use templates right out of the box. For the blog and some pages, we use directly reStructuredText, which is converted to HTML by Pelican.

Besides the template itself, we have written some custom directives in order to give a better appearance to the pages. For example, we can add a header image simply by adding a ``:header:`` tag to the blog entries, just as you see here above. We have also added a custom exercise directive that allows us to write exercises embedded into the page. In a couple of days, we had the system running; the only bugs we faced are design mistakes; fonts too small or too big, etc.

What we like the most is that writing code examples is extremely easy. Adding new features that you want to have systematically included in your entries is very fast, and if you are used to Python you are never leaving your comfort zone. So far we are very happy with the choice. Of course, some things can be improved, and you are more than welcome to point them out if you notice them.

On the downside, as everybody notices after a while, the workflow is not the best. Every time we add a new entry to the blog, we have to recompile the entire website and to upload it to the server. We can streamline it with ``fab``, however, we can do it only from our local computer. Collaborating with others could be achieved through the repository, but we think that in the long term it may become complicated to give the right permissions to everybody in a responsible way. Last but not least, you cannot program entries; you have to be there for updating the website.

Our Verdict
***********
Static websites are not for everybody. If you are writing content rich in code, you can seriously consider it. If you are writing content also in other formats and you wish to have it available online, for example, if you are writing a book and want to transform it into a website, you should at least consider Jinja, it will save you an unimaginable amount of time. So far we are enjoying the process; we like how responsive the website is and we like knowing that we are in control of every detail.

If you want to start fast, however, you need to try another path. Wordpress is very common and easy to use. The wealth of available plugins most likely will solve all your needs. There are also plenty of free and paid templates available; you will always find your way around. The only thing you can't expect from a Wordpress website is a quick response time and to be able to customize the look and feel without getting really involved in the code.

The Links
*********

* Head to `Digital Ocean <https://m.do.co/c/2fbde6232442>`_ if you want to receive a 10€ credit to try out a web server. You are free to do whatever you want, you have root access to it. I have learned a lot thanks to them.
* `Dreamhost <https://www.dreamhost.com/r.cgi?181470/promo/dreamsavings50>`_ is your place if you want to register a domain and get all the perks of a hosting company: domain registration, webmail, and amazing support. Click the link to get 50€ credit on your first purchase of an annual plan (from 97 down to 47€).
* `Pelican <https://blog.getpelican.com/>`_ is the library I use for building this website.
* `Jinja <http://jinja.pocoo.org/>`_ is the library for working with templates.
* Example of how to build a `simple plugin <https://github.com/uetke/website/blob/master/plugins/excercises_directive.py>`_.


Header Photo by `Lukas Blazek <https://unsplash.com/photos/mcSDtbWXUZU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`_ on Unsplash