## Overview



This repository contains information and examples on the use of processes and signals in bash.
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/d8ecfe9109334898b9540ffd20cf64d1c06f0c09.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230127%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230127T155400Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1551c18ee845fd4ebee2b05f242be9f70f08991ff28deed4162b2d3baaa41725"




## Processes



In bash, a process is a program or script that is currently running. Each process is assigned a unique process ID (PID) for identification.



To view all running processes, use the command `ps` or `top`. To view information about a specific process, use the command `ps -p PID` or `top -p PID`.



To start a new process, use the command `command &`, where `command` is the program or script you wish to run. This will run the command in the background, allowing you to continue using the terminal while the process runs.



To stop a running process, use the command `kill PID`, where `PID` is the process ID of the process you wish to stop.



## Signals



A signal is a message sent to a process to indicate a specific event or request. Signals can be sent using the `kill` command, with the signal specified using the `-s` option.



For example, to send the `SIGINT` signal (which indicates that the process should terminate) to a process with PID 123, use the command `kill -s SIGINT 123`.



Common signals include:

- `SIGINT`: terminate the process

- `SIGKILL`: forcefully terminate the process

- `SIGSTOP`: stop the process

- `SIGCONT`: continue a stopped process



To view a list of available signals, use the command `kill -l`.



## Additional Resources



- [Bash Process Management](https://ryanstutorials.net/bash-scripting-tutorial/bash-process-management.php)

- [Linux Signals](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_12_02.html)

- [kill command man page](http://manpages.ubuntu.com/manpages/xenial/man1/kill.1.html)


