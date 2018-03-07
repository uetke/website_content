The Importance of Doing a Backup
================================

:tags: backup, rsync, recovery
:og_description: Back ups are a solution to the most common problems with computers; however almost everybody fails to do them.
:header: {attach}external_drive.jpg
:date: 2018-02-19
:author: Aquiles Carattino

The ransomware attacks that occurred some months ago triggered a wave of people concerned about backups, finally! Ransomware attacks encrypted entire hard drives and the only way of recovering the data was by paying money to the hackers. This kind of attack is simply bypassed by a good back up policy, that enables to recover the system in a short period of time.

However, people who were not involved in ransomware attacks may have not fully comprehended the risks that not having a backup implies. I have seen people losing months of their Ph.D. because of losing data due to a corrupt hard drive. And still, the colleague sitting next door didn't learn from others' mistake and doesn't have any sort of backup.

Having a backup is only a matter of security and minimizing risks. If you know that losing all the data in your hard drive will not set you back for a long time, then you are good as you are; however, I really doubt that you have a computer full of useless information. If losing data will set you back a considerable amount of time, then you should put a mechanism in place to minimize that risk. Ransomware is only one of the problems you may face; data corruption or hardware loss are two of the most common.

A backup is not an external drive with all your files. I have seen people crying because they lost their backup, while in reality, it was only an external drive. There was no other copy of the information in any other place. A backup is a copy of your files, a second, third, fourth copy, but not the only one. If your laptop doesn't have enough capacity, buy two external hard drives; one for backing up, one for expanding the memory.

Keeping the backup and the computer in the same place may not be the best idea. I have a friend who suffers a robbery at his place; both computer and hard drive with the backup were gone. A fire, a flood, an earthquake, anything that can destroy your computer can also destroy your backup. I never feel more vulnerable than when traveling and carrying both backup and computer together.

To have a backup in a different location than your computer, there are several options. First, the obvious one is to leave a second hard drive somewhere else. You could backup your home computer to an external drive and leave it at the office. You could give it to a friend, etc. This is the lowest tech solution, but it is effective. Are you worried about people spying on your files? You should! That is why you can encrypt your backup, but more on that later.

If you are looking for a more elegant solution, you can always opt for hosting your backup in the cloud. I am a person who likes being in control, and therefore I have chosen the `DreamHost Cloud <https://www.dreamhost.com/r.cgi?181470>`_. For only U$4.50 dollars per month, you get 200GB of storage space check the options where it says Dream Objects. Since I run Linux, I simply use `duplicity to perform periodic, incremental backups <https://www.dreamhost.com/blog/backing-up-to-dreamobjects-with-duplicity>`_. If you are a Windows user, you can simply use `Cloud Berry <https://www.cloudberrylab.com/solutions/dreamobjects>`_ for backing up.

.. image:: {attach}hard_drive.jpg
   :alt: Close up of a hard drive in action

Leaving your data unencrypted in an accessible medium is a big risk. It doesn't matter if the NSA is after you or not, you shouldn't leave your data out in the open. With a bit of knowledge, anyone could steal passwords, bank security codes, or even your identity. When you use a remote backup, be sure you use software that encrypts the data before sending it over the network. Duplicity does that automatically, the same with Cloud Berry. It is pretty much the same than what ransomware attackers do: without the proper password, all the files become useless.

By chance, I've encountered two different podcasts where they were trying to recover old bitcoin accounts that could have stored tens or hundreds of thousands of dollars. Bitcoins can be stored on your own computer, and therefore they are subject to the same rules than any other kind of data. If you would have known some years ago that a folder in your computer would be worth a lot of money, wouldn't you have invested in a backup plan?

Traditional backups of copying gigabytes of information over and over are not the only, operational alternative. Imagine you are writing your Ph.D. thesis. You have been working for months on a single document and suddenly it gets corrupted; gone. If you would have been using a version control software, such as Git, you could have been doing off-site backups very often. Without even considering all the advantages that Git poses, you have gotten a copy of your file in a remote location that you could have used to keep working.

Despite the fact that backups are easy to do, relatively cheap (if not free), a lot of people fail in seeing the importance. I think we put too much faith into the status-quo and do not do a proper risk analysis. For 100€ you get an amazing external drive; in less than an hour, you learn how to use rsync for backups. Wouldn't that investment outweigh the costs of a sudden hard drive failure?

Remember, when you were warned and you were given the tools, lamenting is not an option.

Photos by `Andrew Neel <https://unsplash.com/@andrewtneel>`_ and `Patrick Lindenberg <https://unsplash.com/@heapdump>`_ on `Unsplash <https://unsplash.com>`_
