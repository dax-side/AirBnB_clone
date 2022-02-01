#!/usr/bin/python3

""" Entry point to the command interpreter """

import cmd
from models.base_model import BaseModel
import models


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

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
            saves it (to JSON file) and prints the id.
        """
        args = check_input(arg)
        if args is not None and args[0] == "BaseModel":
            bm = BaseModel()
            models.storage.save()
            print(bm.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based
            based on the class name and id.
        """
        args = check_input(arg)
        if args is not None:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                key = "BaseModel." + args[1]
                check_key(key, cmd="show")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = check_input(arg)
        if args is not None:
            if len(args) == 1:
                print(" ** instance id missing **")
            else:
                key = "BaseModel." + args[1]
                check_key(key, cmd="destroy")

    def do_all(self, arg):
        """ Prints all representations of all instances based on
            or not on the class name.
        """
        if arg == "BaseModel" or arg == "":
            odict = models.storage.all()
            for obj in odict.keys():
                objs = odict[obj]
                print(objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
            adding or updating attribute(saves the change into JSON file).
        """
        args = check_input(arg)
        if args is not None:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                key = "BaseModel." + args[1]
                obj = check_key(key, cmd="update")
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    if args[2] in obj.__dict__.keys():
                        vtype = type(obj.__dict__[args[2]])
                        obj.__dict__[args[2]] = vtype(args[3]).strip('"')
                    else:
                        obj.__dict__[args[2]] = args[3].strip('"')
                models.storage.save()
                        

def check_input(arg, **kwargs):
    """ Check if class name is given and it exists """
    args = arg.split()
    if len(args) < 1:
        print("** class name missing **")
    elif args[0] != "BaseModel":
        print("** class doesn't exist **")
    else:
        return args

def check_key(key, **kwargs):
    """ checks whether the id exists """
    try:
        odict = models.storage.all()
        obj = odict[key]
        if kwargs["cmd"] == "show":
            print(obj)
        elif kwargs["cmd"] == "destroy":
            del odict[key]
            models.storage.save()
        elif kwargs["cmd"] == "update":
            return obj
    except KeyError:
        print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
