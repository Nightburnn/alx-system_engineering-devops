What I learned from this project
At the end of this project you are expected to be able to explain to anyone, without the help of Google:
Linux file permissions
Yup. Learned a lot of them.

What do the commands chmod, sudo, su, chown, chgrp do?
chmod - changes mode like change user or groups permissions. sudo is a one time use of su and asks and does 1 super user command. su is when you become a superuser (this is very dangerous if you don't kow your stuff). chown is change ownership. chgrp is change group.

How to represent each of the three sets of permissions (owner, group, and other) as a single digit?
7 is rwx all. 6 is rw- all. 5 is r-x a. 4 is r-- ugo. 3 is -wx all. 2 is -w- ugo. 1 is --x for all. 0 is no permissions, ---.

How to change permissions, owner and group of a file?
chmod, chown, chgrp. Examples are chmod u+x <FILENAME> and that gives the user/ owner of the file execute permissions. chown bryan:holberton danceWithTheDead will change the danceWithTheDead file owner to bryan and the group to holberton. chgrp monkeyDLuffy Jinbei will change the file Jinbei to the monkeyDLuffy group (or the Straw Hats).

Why can’t a normal user chown a file?
Because bad things can happen. The user can give away important files which is very bad. Only the root or su should have that power. But no one man should have all that power.

How to run a command with root privileges?
su or sudo. su will promt you to enter root password and sudo will promt you to enter your own password.

How to change user ID or become superuser?
su to become super user, usermod -u NEWuserID OLDuserID. u flag is UID and l flag is loginUserName. And example is usermod -l Caitlyn Bruce.

How to create a user?
"sudo useradd USERNAME" should work. Adding a -m flag will create a home dir if it does not exist.

How to create a group?
sudo groupadd eliteTen. That should create a new eliteTen group who can take down Azami. Or sudo groupadd Avengers and that should stop Loki and Ultron but oh man Thanos. He curb stomped their faces.

How to print real and effective user and group IDs?
id prints them out. Adding the flags -g shows effective group, -G for all group IDs, -r for real ID, -n for name instead of number, -u for effective user ID.

How to print the groups a user is in?
id -G.

How to print the effective userid?
id -u.
