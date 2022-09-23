What I learned from this project
At the end of this project you are expected to be able to explain to anyone, without the help of Google:
What are the /etc/profile file and the /etc/profile.d directory?
profile sets the environment variables at start up of bash shell and profile.d contains other scripts that are loaded via profile which makes them a part of them kinda. profile will execute scripts within profile.d/.sh and you should place configurations within profile.d.*

What is the ~/.bashrc file?
bashrc also executes the shell scripts within profile.d but only if the users shell is a Interactive Shell (Login Shell). profile calls on basic directly. So Bash runs bashrc only when it is started interactively. It provides a place where you can set up variables, functions, and aliases, define PS1 prompt, and define other settings.

What is the difference between a local and a global variable?
Scope / Accessibility. Stack vs Heap. Initials values are different (garbage vs 0)

What is a reserved variable?
A word that cannot be used as an identifier or variable name or other assignment. Keywords that have a special meaning and the code knows it. Like you can't say "var if = char" or const switch = else;".

How to create, update and delete shell variables?
They can only contain alphanumeric and _. Use command line substitution, "echo $" to view it. To view them all we can just type set, env, or printenv into the terminal. To create is to set. set NAME=VALUE or env NAME=VALUE. To set the variable globally we need to type "export NAME=VALUE". So I 'set five=5' and then I 'export five=5' and now my 'echo $five' works. To update we need to just type the name equals new value like "VARIABLE=newVALUE" so 'five=6' and calling 'echo $five' now prints 6. Now to delete you need to unset. "unset five" then "echo $five" will print out nothing.

What are the roles are the following reserved variables: HOME, PATH, PS1?
HOME is the login dir. The repo for the user's personal files. First dir that a user is in. Go input some commands in. It is convenient and safe for the OS. PATH is not path. PS1 is prompt string 1. This is a built in shell variable that has the login info, what machine logged, pwd, user or super user. An example of just logging in is [surendra@linuxnix common]$. We know surenda is the user who logged on a machine named linuxnix to the pwd of common and is a normal user($). Superusers have #. PS2, 3, 4 exists. There are a lot of control commands for PS1.

What are special parameters?
Parameters that can only be referenced and not assigned. * expands positional parameters. @ expands positional parameters. Differences within quotes and other stuff exist. # expands the number of parameters in decimal. ? expands to the exit status of the most recently executed foreground pipeline. - expands current flag option. $ expands to the process ID of the shell. ! expands to the process ID of the job most recently placed into the background. 0 expands the name of the shell or shell script. This is set at shell initialization and usually 0 is set to the filename used to invoke bash. _ expands to the last argument to the previous command after expansion. Also set to the pull pathname used to invoke each command. Useful for mail purposes.

What is the special parameter =$?
The parameter ? expands the exit status of the most recently executed foreground pipeline.

What is expansion and how to use them?
*An example of an expansion is . With expansion when I type something and it is expanded into something else before the shell acts upon it. Expansion can be used like grep. We have pathname expansion, tilde expansion, arithmetic expansion, brace expansion, parameter expansion, and command substitution. Use them with wildcards for maximum omg.

What is the difference between single and double quotes and how to use them properly?
Single quotes will not interpret the code so echo '$(echo "poop")' will output (echo "poop"). Double quotes will interpolate which means echo "(echo "YASSS 4 star!")" will print out YASSS 4 star!

How to do command substitution with $() and backticks?
Well first the syntax is $(command-name) and command-name. Next, an example, echo -e "List of users logged on:\n $(w)".

How to perform arithmetic operations with the shell?
$((expression)). PEMDAS. Don't forget dat. Example, echo 2 plus 2 is 4, minus 1 dats $((2+2-1)) quick maffs! Skrrat, skid-kat-kat boom! GOD I AM HAHAALARIOUS.

How to create an alias?
Open up bashrc and do some magic. Then do alias aliasNAME='commands'. Now all you gotta do is type aliasName and the commands will run.

How to list aliases?
Type alias in the command line.

How to temporarily disable an alias?
Prefix the alias with a backslash so \alias should not work. Or put it in some quotes or write command before it.

How to execute commands from a file in the current shell?
*source ./fileNAME *

*What happens when you type $ ls -l .txt?
No such file or directory. But if i did have any files that ended with .txt it would show in long format.
