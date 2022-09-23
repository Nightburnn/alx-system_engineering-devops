What I learned from this project
At the end of this project you are expected to be able to explain to anyone, without the help of Google:
What do the commands head, tail, find, wc, sort, uniq, grep, tr do?
head outputs the first part of the files (default 10 lines). So “head -n99 beer wall” gives the first 99 lines from the files beer and wall. The -c flag will give back bits while -n is lines. tail is the same as head but for lines at end of file. find searches and locates lists of files and dir based on conditions I set. find -name works and other flags will be useful like -f for type or -perm for permissions or -user for user or -group for group or -mtime # for days modified # of days back or -atime # for accessed # of days back or -cmin or -mmin and a whole bunch of other good flags. wc is word count. wc -lwcmL is for lines, words, bytes, chars, or length of longest line. sort sorts. sort will rearrange the lines in a .txt file so they are numerically and alphabetically sorted. Some rules are number before letters and lowercase before the uppercase (eg. a A b c C z). Lots of good flags for this one including ignoring blanks and merge files. uniq reports or filters out repeated lines in a file. Most popular flags outs probably be -cdu. grep is regex. I can type ‘grep “stringConstant filename.’ Lots of good flags for this like case insensitive search, recursive search, show which lines do not match, etc. tr is for translating, deleting or squeezing repeated chars. Very useful for replacement text by default. “tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ” will convert all to uppercase. [:lower:] and [:upper:] works too. So do a-z and A-Z.

How to redirect standard output to a file?
> will redirect output. 1> is default which is display stdout and 2> is stderr. cat > box.txt [INPUT] will overwrite INPUT into box. > will override and >> will append.

How to get standard input from a file instead of the keyboard?
< will work. So I can do “sort < gotei13.txt” and that should sort all the captains instead of me manually inputting all their names.

How to send the output from one program to the input of another program?
*< and > will do the work. Need to change flags or other stuff depending on the goal. Also piping should work too, |. *

How to combine commands and filters with redirections?
You just pipe or connect them with |, <, >. Logic.

What are special characters?
Characters that carry out a special instruction or have a different meaning than we intend them to, also known as meta-characters.

Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them?
Done. White space is to determine when things begin and end. Single quotes are string literals so special characters inside them are ignored. Double quotes prevent the text inside from being split into multiple but it does allow command line substitutions. Backslash prevents the next char from being interpreted as a special character. comment is # so # wouldn’t be a comment. Pipe redirects output from an initial common to the input of a secondary command, used to chain commands together. Command separator is ;. It is common for IF THEN statement and it represents a newline. Tilde is ~. ~ is the home directory.

How to display a line of text?
We can use cat to display the file or cat -n to display the first to nth lines. Or we can use sed. sed -n 5p filename will print out line 5 of filename.

How to concatenate files and print on the standard output?
cat file1.txt file2.txt file3.txt…

How to reverse a string?
Examples include echo “STRING” | rev or rev<<<“STRING”. There are other ways too.

How to remove sections from each line of files?
*cut. I am Bon Qui Qui and I will cut you. We can cut the nth byte, or character, or other ways with a lot of diff flags. I can use sed also to do some magic, maybe. *

What is the /etc/passwd file and what is its format?
It has login info of users. 7 fields on each line, first is account name, second is placeholder for password info (obtained in etc/shadow), third is User ID and the root is always UID 0, 4th is group ID, 5th is comment field, 6th is home dir (usually /home/username since we ain’t root people), 7th is user shell like bin/bash. This field contains the shell that will be spawned.

What is the /etc/shadow file and what is its format
The passwords. Long ago passwords use to be hashed in the /passwd file but lots of people have read permissions there so dat hella bad. The keys are not stored in plain text or at least they shouldn’t be. This place should have key derivation functions to make a new hash. This file should be unreadable by unprivileged users. There is a shadow group and they have read permissions. 7 password fields and they are defined. First is daemon or account username. Second is salt and hashed password. 3rd is last password change date, measures in unix epoch time. 4th is the days until password change is permitted (0 means no restrictions). 5th is days until password change is required and 99999 means there is no limit. 6th is the days of warning prior to expiration (useful for password change requirement workplaces). 7th is kinda blankish sometimes. The last 3 fields denote days before the account was inactive, days since the Epoch when the account expires, and last field is unused.
