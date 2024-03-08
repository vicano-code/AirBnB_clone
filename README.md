## AirBnB_clone

### Description
> The goal of the AirBnB clone project is to deploy on a server a simple copy of the AirBnB website.
> This is the first phase of the AirBnB clone project - the console.
> This repository contains several class files and the command interpreter file.
> The command interpreter acts like a shell. It is used to perform tasks and manipulate object instances. 
> The command interpreter was coded to work in both interactive and non-interactive modes.
> The code functionality was unit-tested with the python unittest module

### Installation
```
git clone https://github.com/vicano-code/AirBnB_clone.git
cd AirBnB_clone
```

### Using the command interpreter
Interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Environment
* Language: Python3 (version 3.8.5)
* OS: Ubuntu 20.04 LTS

### Authors
* Victor C. Anokwuru
* Olawale Abdullahi
