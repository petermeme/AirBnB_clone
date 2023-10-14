#!/usr/bin/python3
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

    patterns = {
        'all': r'^([A-Za-z]+)\.all\(\)$',
        'count': r'^([A-Za-z]+)\.count\(\)$',
        'show': r'^([A-Za-z]+)\.show\((["\'\w-]+)\)$',
        'destroy': r'([A-Za-z]+)\.destroy\((["\'\w-]+)\)',
        'update': r'^([A-Za-z]+)\.update\((["\'\w-]+), (["\'\w_]+), '
                  r'([" \'\@\$\w_\.-]+)\)$',
        'update_from_dict': r'^([A-Za-z]+)\.update\((["\'\w-]+), (\{.*?\})\)'
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def split_arg(self, arg):
        """Split the line in to substrings based on double quotes and spaces"""
        pattern = r'(?:"[^"]+"|\S+)'
        return re.findall(pattern, arg)

    def do_create(self, arg):
        """Creates an instance of the passed class if it exists,
        saves it and prints its id"""
        arg = self.split_arg(arg)
        if not arg:
            return print("** class name missing **")
        klas = arg[0]
        if klas not in self.__classes:
            return print("** class doesn't exist **")
        obj = eval(klas)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """prints the string representation of an instance"""
        arg = self.split_arg(arg)
        if not arg:
            return print("** class name missing **")
        if arg[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(arg) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(arg[0], arg[1])
        instance = storage.all().get(key)
        if not instance:
            return print("** no instance found **")
        print(instance)

    def do_destroy(self, arg):
        """deletes an instance given a classname and instance id"""
        arg = self.split_arg(arg)
        if not arg:
            return print("** class name missing **")
        if arg[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(arg) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(arg[0], arg[1])
        instance = storage.all().get(key)
        if not instance:
            return print("** no instance found **")
        del storage.all()[key]

    def do_all(self, arg):
        """prints all instances of a given model"""
        arg = self.split_arg(arg)
        if not arg:
            return print("** class name missing **")
        klas = arg[0]
        if klas not in self.__classes:
            return print("** class doesn't exist **")
        instances = [str(instance) for k, instance in storage.all().items() if
                     k.startswith("{}.".format(klas))]
        print(instances)

    def do_update(self, arg):
        """updates a model instance"""
        arg = self.split_arg(arg)
        if not arg:
            return print("** class name missing **")
        if arg[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(arg) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(arg[0], arg[1])
        instance = storage.all().get(key)
        if not instance:
            return print("** no instance found **")
        if len(arg) < 3:
            return print("** attribute name missing **")
        if len(arg) < 4:
            return print("** value missing **")
        try:
            value = eval(arg[3])
        except (NameError, SyntaxError):
            value = arg[3]
        setattr(instance, arg[2], value)
        instance.save()

    def custom_eval(self, arg):
        """Processes a value to be parsed to do_update"""
        arg = str(arg)
        if arg.replace('.', '', 1).isdigit():
            return str(arg)
        return '"{}"'.format(arg)

    def onecmd(self, line):
        """Override to handle advanced commands"""
        # Model.all
        match = re.search(self.patterns['all'], line)
        if match:
            klas = match.group(1)
            return self.do_all(klas)
        # Mode.count
        match = re.search(self.patterns['count'], line)
        if match:
            klas = match.group(1)
            if klas in self.__classes:
                return print(len([str(instance) for k, instance in
                                  storage.all().items() if
                                  k.startswith("{}.".format(klas))]))
        # Model.show
        match = re.search(self.patterns['show'], line)
        if match:
            klas = match.group(1)
            uid = eval(match.group(2))
            return self.do_show("{} {}".format(klas, uid))
        # Model.destroy
        match = re.search(self.patterns['destroy'], line)
        if match:
            klas = match.group(1)
            uid = eval(match.group(2))
            return self.do_destroy("{} {}".format(klas, uid))
        match = re.search(self.patterns['update'], line)
        # Model.update
        if match:
            klas = match.group(1)
            uid = eval(match.group(2))
            attribute_name = eval(match.group(3))
            value = match.group(4)
            command = "{} {} {} {}".format(klas, uid,
                                           attribute_name, value)
            return self.do_update(command)
        # Model.update with dict
        match = re.search(self.patterns['update_from_dict'], line)
        if match:
            klas = match.group(1)
            uid = eval(match.group(2))
            kw = eval(match.group(3))
            for k, v in kw.items():
                self.do_update("{} {} {} {}".format(klas, uid, k,
                                                    self.custom_eval(v)))
            return
        return super(HBNBCommand, self).onecmd(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
