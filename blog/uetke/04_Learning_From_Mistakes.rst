Learning From Mistakes
======================

:author: Aquiles Carattino
:date: 2018-07-23
:subtitle: The Cost of Learning From Mistakes
:header: {attach}mistakes.jpg
:tags: Uetke, Cookies, Privacy, Tracking
:og_description: The Cost of Learning From Mistakes

A child project of Uetke is `Python For The Lab <https://www.pythonforthelab.com>`__, a website where you can find articles about Python programming and a `Forum <https://forum.pythonforthelab.com>`_ to evacuate your doubts. We had also included a newsletter sign-up form, similar to the one you find here on the right or at the bottom of the page. When deciding how to develop the websites, we went for the full experience: built almost everything by ourselves.

Static websites are fashionable these days, mainly because they are very low maintenance. You can receive a high amount of visitors in cheap servers, without the risk of compromising data or infrastructure. We built our workflow on top of `Pelican <https://blog.getpelican.com/>`__, a Python-based library for generating static websites. We had to build the template ourselves, including special plugins for working with header and social images, etc.

It was a process of great learning because we were completely out of our comfort zone. A website is like a window where you show yourself, therefore you need to make it look as good as you can. Optimizing for mobile phones, optimizing for high-density displays, learning about CSS, and, fundamentally, about Javascript. The scripting language that powers the web can also become the worst nightmare of a young website.

Static websites offer little interactivity with the visitors. Newsletters, comments, feedback, etc. all have to be handled in a different server. In the beginning, we had just one small box to allow users to sign up for a newsletter. However, this box was not visible on mobile phones, the platform of choice of our users. We added a second box at the bottom of the article pages, which looks exactly the same. Actually, it was *the same box*.

The number of sign-ups to our newsletter didn't improve. We had some very successful articles, with thousands of visitors, but not a single subscription. It is very hard to predict user behavior, so we assumed it was just that people were not interested in our newsletter. Curious enough, with much fewer visitors, Uetke.com was receiving a constant stream of sign-ups.

Oh, Javascript. In order to explore how to grow the number of sign-ups, we started exploring the possibility of adding a pop-up window to the articles. And that was the moment of realization. It was not working. Javascript doesn't issue warnings, it just silently doesn't do what you were expecting. The reason was that two different elements on the page had the same ``id``, and Javascript didn't know how to handle that situation.

We have fixed that on `Python For The Lab <https://www.pythonforthelab.com>`__ and now our numbers are increasing steadily. Considering the time this bug was around and our conversion rates, we lost a significant amount of sign-ups to our newsletter. Our core business lays somewhere else completely, therefore it wasn't a big deterrent. However, such a small mistake can have a huge impact if it happens in the wrong place.

We have learned several valuable lessons. Of course, we have learned about website creation and Javascript, but we have also learned about the risks of stretching yourself outside of your capabilities. A professional website developer, we want to believe, would have never made that mistake. That is the value we deliver to our customers. Years of accumulated experiences allow us to deliver software with a much higher quality than what can be developed in-house.

If that newsletter would have been a central part of our strategy, it would have been a gigantic setback. Investing in professional support would have paid off in no time. Scientific software plays the same role.


Header photo by `Estée Janssens <https://unsplash.com/photos/RARH8b7N-fw?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`_ on Unsplash