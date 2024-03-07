#!/usr/bin/python3
"""
 contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter for the AirBnB console"""

    prompt = "(hbnb) "

    def emptyline(self):
        return

    def do_quit(self, arg):
        '''Quits the command interpreter\n'''
        return True

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
