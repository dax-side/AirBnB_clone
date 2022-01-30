#!/usr/bin/python3

""" Entry point to the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Entry point to the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        ''' EOF command to exit the program'''
        exit()

    def do_quit(self, arg):
        """ Quit command to exit the program """
        exit()

    def emptyline(self):
        """ Ignores empty lines when passed"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
