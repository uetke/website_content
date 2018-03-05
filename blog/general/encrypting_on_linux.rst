How to Encrypt an External Drive on Linux
=========================================

:subtitle: Keeping your data out of reach is an important safety measure
:status: draft
:date: 2018-03-05
:keywords: safety, encryption, Linux, disk, luks
:header: {attach}encrypt-lock-data.jpg

It has probably happened to you that the data you generate in the lab does not fit on the SSD drive of your ultrabook. You soon realize that not only your scientific data takes up a lot of space, but also your personal information, such as photos and videos. You then buy an external drive, however, as soon as you move your data to the external drive you need to consider that your data becomes available to anybody who has access to it. This is perhaps not what you wish, neither for your lab data nor for your personal information. In a similar manner, when you perform a backup to an external drive, as we discussed in our previous post on `The Importance of Doing a Backup <{filename}backup.rst>`_, you are facing exactly the same problem.

To solve it, in this post we are going to discuss how to encrypt a hard drive on Linux, focusing on Ubuntu/Debian, but other distributions should work in a very similar way. We are going to use `LUKS` for encrypting the device and therefore we need to install it:

.. code-block:: bash

   sudo apt-get install cryptsetup

This is all we should do to install it; Fedora users can install it through ``yum install cryptsetup-luks``. Now, we are going to encrypt the hard drive. When doing it this warning may pop up:

.. warning:: When encrypting your hard drive you will lose all the information contained in it. Be sure you are encrypting the proper partition.

We assume our drive is ``/dev/sdz1``, but you should check where it is. You need to be absolutely sure that you are not encrypting your home partition or a disk with important information. You can see more information about the drives present in your computer by running:

.. code-block:: bash

   ls -l /dev/disk/by-*

You will see all the devices listed and ordered in different ways: by their *UUID*, *path*, etc. Check what is the partition you want to encrypt. Remember that you don't need to encrypt the entire disk, therefore you if want to have a public and a private space run:

.. code-block:: bash

   sudo cryptsetup -y -v luksFormat /dev/sdz1

which will provide a fair warning regarding what we are about to do:

.. code-block:: bash

   WARNING!
   ========
   This will overwrite data on /dev/sdz1 irrevocably.

   Are you sure? (Type uppercase yes): YES
   Enter LUKS passphrase:
   Verify passphrase:
   Command successful.

After you write the passphrase there will be no way of recovering it. If you lose it or forget it you will be locked out from your drive and you will have to format it. Remember that the point of encrypting is to keep people away from your data, including yourself. To mount an encrypted partition we have to do it in two steps: first, we need to decrypt and then we need to mount.

.. code-block:: bash

   sudo cryptsetup luksOpen /dev/sdz1 backup

In this case, we have chosen ``backup`` as the label for our disk, but you can use whatever you want. The command maps our drive but doesn't mount it. Before we can continue, we should format the drive; you can use any filesystem you wish, we will use `ext4`:

.. code-block:: bash

   sudo mkfs.ext4 /dev/mapper/backup

Now we are ready to mount and use our encrypted partition. We mount it as any other device, but using the mapper:

.. code-block:: bash

   sudo mount /dev/mapper/backup /backup

The first ``backup`` is the label we have assigned with the ``luksOpen`` command. The second is the mount point, ``/backup``, that has to exist before mounting, exactly in the same way as with any other device. Now you have your partition mounted and you can use it without any further concerns. If you are on Linux with a user interface, normally you can handle de decryption of the drive with the file manager. It is very straightforward, you just introduce the password when you are asked for it and you use the disk as always.

Finally, to unmount the disk we run:

.. code-block:: bash

   sudo umount /backup
   sudo cryptsetup luksClose backup

.. note:: If you are very conscious about security, you should also hide how much the disk is filled with data. Before mounting the drive, but after decrypting you can run ``sudo dd if=/dev/zero of=/dev/mapper/backup``, which will fill up all the space with zeros. It can take a while to complete depending on the size of your drive.

How to automount an encrypted drive
***********************************
In some cases you would like to be able to automount the drive, i.e., the drive should be available after a reboot of the system. For example, you could have a drive connected to a Raspberry Pi to which you automatically back up all your data while at home. However, the drive should be mounted always at the same location even if the power goes off and there is a reboot. What we are going to do is to generate a new key and we are going to store it on the computer; with that key, we are going to decrypt the drive and mount it automatically.

.. warning:: There are some safety concerns in doing this; anybody with access to the key will be able to access your information. You should decide what are the different scenarios, if someone has physical access to your computer, etc.

We are going to create the key within the `root` user folder, and that user is going to be the only one with access. Proper file permissions can keep the key file safe within your environment, but it doesn't protect it from direct physical access. We first create a new random key by running the following command:

.. code-block:: bash

   sudo dd if=/dev/urandom of=/root/keyfile bs=1024 count=4

The key is going to be very long, much longer than a 20 character password and therefore virtually impossible to guess. We make the file only readable by the root user:

.. code-block:: bash

   sudo chmod 0400 /root/keyfile

We next need to add this file to the LUKS partition:

.. code-block:: bash

   sudo cryptsetup luksAddKey /dev/sdz1 /root/keyfile

Now we can automatically map the disk using that file. You can edit the file ``/etc/crypttab`` with whatever editor you like, and then you add:

.. code-block:: bash

   backup      /dev/sdz1  /root/keyfile  luks

This will map the device ``/dev/sdz1`` to ``/dev/mapper/backup`` by using the ``/root/keyfile``. You can customize whatever you need in this command. You then save the file and close the editor. Once we automatically map the drive, we can also automatically mount it. We modify the file ``/etc/fstab`` with a text editor and we add the following line:

.. code-block:: bash

   /dev/mapper/backup /backup     ext4    defaults        0       2

To check that everything worked, you can automount all the disks:

.. code-block:: bash

   sudo mount -a

Or you can reboot your computer and see that the external drive is mounted. It is a very good idea to always use the UUID of the disk instead of its number. If you add a new drive, it may happen that the numbering changes, while the UUID will stay always the same. You can find the identification of your drive by running:

.. code-block:: bash

   ls -l /dev/disk/by-uuid

Then you can change the file ``/etc/crypttab`` to point to the UUID of your device:

.. code-block:: bash

   backup      /dev/disk/by-uuid/UUID_NUMBER  /root/keyfile  luks

Encrypting is an easy safety measure that we can take with all our information. It prevents strangers to read our files even if they have physical access to our devices. Just note that if you are traveling to the US, you should consider `not bringing any electronics with you <https://www.cbp.gov/newsroom/national-media-release/cbp-releases-updated-border-search-electronic-device-directive-and>`_; if you are found with an encrypted device they can ask you for your password, and if you refuse you will go back to where you came from.


Header photo by `James Sutton <https://unsplash.com/photos/FqaybX9ZiOU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText>`_ on Unsplash
