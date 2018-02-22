Using two different ssh keys for Github repositories
====================================================

:tags: Git, ssh, Key, encription

I have two different users at Github, one is my `personal account <https://github.com/aquilesC/>`_ and the other is the `Uetke account <https://github.com/uetke/>`_. In my personal account I do sometimes play with repositories that nothing have to do with my work and therefore I like keeping things separated. However ssh keys can be used in one account at a time; fortunately the solution is easier than what I would have imaged.

First you setup your new ssh key as you probably did with the first one:

.. code-block:: bash

   ssh-keygen -t rsa -C "my_email@example.com"

and remember to store it with a different name than the previous one. For example I will call each key as follows:

.. code-block:: bash

   ~/.ssh/id_rsa_github1
   ~/.ssh/id_rsa_github2

And add them

.. code-block:: bash

   ssh-add ~/.ssh/id_rsa_github1
   ssh-add ~/.ssh/id_rsa_github2
   ssh-add -D
   ssh-add -l

The last two lines are just for deleting the cached files and then to list the available keys. You can verify that the proper keys were correctly installed by ssh. The last step is to modify the configuration file of ssh to enable the selection of one or the other key:

.. code-block:: bash

   cd ~/.ssh/
   touch config

Open the newly created config file with whatever editor you like and add the following:

.. code-block:: bash

   # Github 1 account
   Host github.com-git1
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_rsa_github1

   #Github 2 account
   Host github.com-git2
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_rsa_github2

The only thing you have to do now is to clone the repository using either github.com-git1 or github.com-git2:

.. code-block:: bash

   git clone git@github.com-git1:User1/repo.git

You can also add it as a remote:

.. code-block:: bash

   git remote add git@github.com-git2:User2/repo.git

I use this to update repositories into the Uetke profile once they are ready for the public, but in the meantime I use my personal repository for myself or extremely curious people.