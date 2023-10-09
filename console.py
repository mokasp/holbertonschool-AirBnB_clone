#!/usr/bin/python3
""" Module containing the class HBNBCommand """
# Michael Updated at 1:50 PM 10/8
import cmd
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A class that runs the AirB&B Console
    As the entry point to the command interpreter

    Attributes
    ~~~~~~~~~~
    prompt (string):
        Displayed as the cursor for the user.
    classes (dictionary):
        All subclasses available for the user to call.

    Methods
    ~~~~~~~
    do_emptyline():
        Do nothing when an empty line is entered.
    do_quit():
        Exits the program when called by the user.
        User Command - quit
    do_EOF():
        Enter the command "EOF" to quit the program
        Handles CTRL+D
        User Command - EOF
    do_create():
        Enter the command "create <class>" to make a new Object.
        User Command - create <class>
    do_show():
        Enter the command "show <class> <id>" to display
        that specific object.
        User Command - show <class> <id>
    do_destroy():
        Enter the command "destroy <class> <id>" to remove
        that specific object.
        User Command - destroy <class> <id>
    do_all():
        Enter the command "all" to print everything in storage.
        Enter the command "all <class>" to print anything created
        with that class.
        User Command - all OR all <class>
    do_update():
        Enter the command:
        update <class> <id> <new attribute> "<new attribute value>"
        to add a new attribute to an instance of the specific class.
        User Command -
        update <class> <id> <new attribute> "<new attribute value>"
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, line):
        """
        Enter the command "quit" to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Enter the command "EOF" to quit the program
        Handles "CTRL D"
        """
        return True

    def do_create(self, line):
        """
        Enter the command "create <class>" to make a new Object.
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        object_type = args[0]
        try:
            new_object = self.classes[object_type]()
            models.storage.save()
            print(new_object.id)
        except KeyError:
            print("** class doesn\'t exist **")

    def do_show(self, line):
        """
        Enter the command "show <class> <id>" to display
        that specific object
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_of_them = models.storage.all()
        try:
            print(all_of_them[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Enter the command "destroy <class> <id>" to remove
        that specific object
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn\'t exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            dictionary = models.storage.all()
            dictionary.pop(key)
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Enter the command "all" to print everything in storage.
        Enter the command "all <class>" to print anything created
        with that class.
        """
        args = line.split()
        dictionary = models.storage.all()
        instance_list = []

        if len(line) == 0:
            for key in models.storage.all():
                print(models.storage.all()[key])
        elif args[0] not in self.classes:
            print("** class doesn\'t exist **")
            return
        else:
            for key in dictionary:
                var = key.split(".")
                if var[0] == args[0]:
                    instance_list.append(str(dictionary[key]))
            print(instance_list)

    def do_test(self, line):
        """
        TEST STUFF
        """
        print(models.storage.__class__.__name__)

    def do_update(self, line):
        """
        Enter the command:
        update <class> <id> <new attribute> "<new attribute value>"
        to add a new attribute to an instance of the specific class.
        """
        args = line.split()
        key = f"{args[0]}.{args[1]}"
        dictionary = models.storage.all()
        if len(line) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn\'t exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif key not in dictionary:
            print("** no instance found **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        the_object = dictionary.get(key)
        strings = re.findall('"([^"]*)"', line)
        setattr(the_object, args[2], strings[0])
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
