#!/usr/bin/env python
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    @property
    def implemented_models(self):
        return ['BaseModel']

    @staticmethod
    def print_error(msg):
        print(msg)

    def do_create(self, arg):
        """Creates an instance of the passed class if it exists,
        saves it and prints its id"""
        if not arg:
            return self.print_error("** class name missing **")
        if arg not in self.implemented_models:
            return self.print_error("** class doesn't exist **")
        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """prints the string representation of an instance"""
        if not arg:
            return self.print_error("** class name missing **")
        args = arg.split()
        if args[0] not in self.implemented_models:
            return self.print_error("** class doesn't exist **")
        if len(args) < 2:
            return self.print_error("** instance id missing **")
        key = "{}.{}".format(args[0], args[1])
        instance = storage.all().get(key)
        if not instance:
            return self.print_error("** no instance found **")
        print(instance)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
