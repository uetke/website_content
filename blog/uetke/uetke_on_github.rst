Uetke's website is also on Github
=================================

:subtitle: The website is built thanks to Pelican and static files
:status: draft
:date: 2018-02-26
:og_description: You can see the code that sustains the website directly at Github

To honor the spirit of all what we do at Uetke, I figured it would have been a good idea to make all the under-the-hood code freely available for others to read, learn, and improve. The code is hosted at Github in two different repositories: `the content <https://github.com/uetke/website_content>`_ and the `style files <https://github.com/uetke/website>`_. We have decided to build Uetke on Pelican, a Python generator of static websites, and therefore you can find the plain files in the content and the template and configuration files in the other.

Some months ago I've realized the website was having some issues regarding speed and server usage. It was taking too long to load, regardless of where in the world you were located. Wordpress is a great tool but it has become so complex over the years that it results hard to improve with little knowledge. On top of things, I was using Divi, an Elegant Themes template that was loading a host of files from other servers and was generating a lot of complex syntax in my pages; moving to a different template was not an easy solution.

Static websites were always an option, but I thought they were suitable for another kind of situations until I decided to give them a try. The obvious advantage of static websites is that the requirements for the web server are minimal; there is no workload on the server side, only serving plain files to users. The downside is that you can't have interaction with your users, such as contact forms without relying on external providers. I could work with that; my priority was to have a fast website and a cheap server.

If you look around for a course on how to build a website with Bootstrap, the CSS template made available by Twitter, you will notice a complete absence of examples on how to build templates. I mean, websites have common elements through their pages, and therefore it would make sense to import those elements and not to copy paste and update in a million different files. I felt that all the courses were falling very short for someone who is planning to work in the real-world with plain HTML.

To solve the problem I started to look into Jinja, a Python library for using templates. The beauty of Jinja is that you can use templates for anything, not only websites. If you want to use Jinja for your latex files, for example, you can use it. Jinja is very extensible and complex; reading the documentation is very important. At the same time I realized I was using reStructuredText for documenting the software I was developing, and therefore it would have made sense to keep everything with the same format, simplifying the copy and paste.

At that moment was when Pelican popped up; it is designed as a blogging platform that can transform plain text files into HTML pages. You can use Markdown or reStrcturedText for your text files. There are templates based on Jinja and plugins to expand the functionality. Moreover, since it is built on top of common Python libraries, you can write your own plugins and expansions quite easily; you only have to get acquainted with the terminology.

The Final Setup
***************
Since the majority of the visitors to the website come from The Netherlands, I decided to have my server in Amsterdam. I am using `Digital Ocean <https://m.do.co/c/2fbde6232442>`_ with the smallest plan. At 5€/month is not at all a bad deal and it provides enough power to host this and other websites. By the way, if you click `the link <https://m.do.co/c/2fbde6232442>`_, you get 10€ credit to start trying it out. I `installed and configured nginx <https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04>`_ and added `SSL encryption <https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04>`_. It takes a while to learn, but it is very gratifying.

To register the domain and hosting the e-mail I've used `Dreamhost <https://www.dreamhost.com/r.cgi?181470/promo/dreamsavings50>`_. I've been their customer for over 10 years and I have never been disappointed. Of course, you can opt to host your website directly with them and it will work more than fine. I just wanted to embark on the adventure of managing my own web server. If you click on `the link <https://www.dreamhost.com/r.cgi?181470/promo/dreamsavings50>`_ you will get a 50U$ discount when signing up for a yearly plan. At 97U$ (or 47U$ with the discount) for a full year of unlimited hosting, webmail, etc. you won't find a better solution around.

For the website itself, I built a lot of HTML pages that are the ones you see when browsing the site. The courses, the contact us, etc. They are rendered by Pelican when compiling the website, and the main advantage is that I could use templates right out of the box. For the blog and some pages, I use directly reStructuredText, which is converted to HTML by Pelican.

Besides the template itself, I have written some custom directives in order to give a better appearance to the pages. For example, I can add a header image simply by adding a ``:header:`` tag to the blog entries, just as you see here above. I have also added a custom exercise directive that allows me to write exercises embedded into the page. In a couple of days, I had the system running; the only bugs I faced are design mistakes; fonts too small or too big, etc.

What I like the most is that writing code examples is extremely easy. Adding new features that you want to have systematically included in your entries is very fast, and if you are used to Python you are never leaving your comfort zone. So far I am very happy with the choice. Of course, some things can be improved, and you are more than welcome to point them out if you notice them.

On the downside, as everybody notices after a while, the workflow is not the best. Every time I add a new entry to the blog, I have to recompile the entire website and to upload it to the server. I can streamline it with ``fab``, but still I can do it only from my computer. Collaborating with others could be achieved through the repository, but I imagine in the long term it may become complicated to give the right permissions to everybody in a responsible way. Last but not least, you cannot program entries; you have to be there for updating the website.

My Verdict
***********
Static websites are not for everybody. If you are writing content rich in code, you can seriously consider it. If you are writing content also in other formats and you wish to have it available online, for example, if you are writing a book and want to transform it into a website, you should at least consider Jinja, it will save you an unimaginable amount of time. So far I am enjoying the process; I like how responsive the website is and I like knowing that I am in control of every detail.

If you want to start fast, however, you need to try another path. Wordpress is very common and easy to use. The wealth of available plugins most likely will solve all your needs. There are also plenty of free and paid templates available; you will always find your way around. The only thing you can't expect from a Wordpress website is a quick response time and to be able to customize the look and feel without getting really involved in the code.

The Links
*********

* Head to `Digital Ocean <https://m.do.co/c/2fbde6232442>`_ if you want to receive a 10€ credit to try out a web server. You are free to do whatever you want, you have root access to it. I have learned a lot thanks to them
* `Dreamhost <https://www.dreamhost.com/r.cgi?181470/promo/dreamsavings50>`_ is your place if you want to register a domain and get all the perks of a hosting company: domain registration, webmail, and amazing support. Click the link to get 50€ credit on your first purchase of an annual plan (from 97 down to 47€).
* `Pelican <https://blog.getpelican.com/>`_ is the library I use for building this website
* `Jinja <http://jinja.pocoo.org/>`_ is the library for working with templates
* Example of how to build a `simple plugin <https://github.com/uetke/website/blob/master/plugins/excercises_directive.py>`_