#!/usr/bin/env python
"""Defines the HBnB console."""
import cmd
import re

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    patterns = {'all': r'[A-Za-z]+\.all\(\)'}

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_create(self, arg):
        """Creates an instance of the passed class if it exists,
        saves it and prints its id"""
        if not arg:
            return print("** class name missing **")
        if arg not in self.__classes:
            return print("** class doesn't exist **")
        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """prints the string representation of an instance"""
        if not arg:
            return print("** class name missing **")
        args = arg.split()
        if args[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(args) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(args[0], args[1])
        instance = storage.all().get(key)
        if not instance:
            return print("** no instance found **")
        print(instance)

    def do_destroy(self, arg):
        """deletes an instance given a classname and instance id"""
        if not arg:
            return print("** class name missing **")
        args = arg.split()
        if args[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(args) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(args[0], args[1])
        instance = storage.all().get(key)
        if not instance:
            return print("** no instance found **")
        storage.delete(key)

    def do_all(self, arg):
        """prints all instances of a given model"""
        if not arg:
            return print("** class name missing **")
        if arg not in self.__classes:
            return print("** class doesn't exist **")
        instances = [str(instance) for k, instance in storage.all().items() if
                     k.startswith("{}.".format(arg))]
        print(instances)

    def do_update(self, arg):
        """updates a model instance"""
        if not arg:
            return print("** class name missing **")
        args = arg.split()
        if args[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(args) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(args[0], args[1])
        instance = storage.all().get(key)
        if not instance:
            return print("** no instance found **")
        if len(args) < 3:
            return print("** attribute name missing **")
        if len(args) < 4:
            return print("** value missing **")
        setattr(instance, args[2], eval(args[3]))
        instance.save()

    def default(self, line):
        """Handle shortcut/customized commands"""
        if line.endswith(".all()"):
            return self.cmdqueue.append("all {}".format(line.split(".")[0]))
        elif line.endswith('.count()'):
            klas = line.split(".")[0]
            matching = [k for k in storage.all().keys() if k.startswith(klas)]
            return print(len(matching))
        super(HBNBCommand, self).default(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
