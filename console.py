#!/usr/bin/python3
"""
this module contains the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class is for a command line interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Uses quit as a command to exit"""
        return True

    def do_EOF(self, arg):
        """command for end of file"""
        return True

    def emptyline(self):
        """empty line"""
        return 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
