#!/usr/bin/python3
""" Module containing the class HBNBCommand """
# Up to date version 2:32 PM
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    A class that runs the AirB&B Console
    As the entry point to the command interpreter

    Attributes
    ~~~~~~~~~~
    prompt (string):
        Displayed as the cursor for the user.

    Methods
    ~~~~~~~
    do_emptyline():
        Do nothing when an empty line is entered.
    do_quit():
        Exits the program when called by the user
    do_EOF():
        Enter the command "EOF" to quit the program
        Handles "CTRL+D"
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def emptyline(self):
        """ Do nothing when an empty line is entered"""
        pass

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """
        Enter the command "EOF" to quit the program
        Handles "CTRL D"
        """
        return True

    def do_create(self, line):
        """
        Create command to make new Object
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        object_type = args[0]
        try:
            new_object = self.classes[object_type]()
            print(new_object.id)
        except KeyError:
            print("** class doesnt exist **")

    def do_show(self, line):
        """
        Show command to display an object
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
        """ Destroy command to remove an object from storage
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
        try:
            del models.storage[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")
    
    def do_all(self, line):
        """
        All command to display all objects, or all instances of a specific\
        class, in storage """
        if len(line) == 0:
            for key in models.storage.all():
                print(models.storage.all()[key])
        else:
            args = line.split()
            print("~~~ im stuck here ~~~")

    def do_update(self, line):
        """
        Update command to add attributes to existing objects
        """
        print("update")
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_of_them = models.storage.all()
        try:
            print(all_of_them[key])
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** ~THIS ONE NEEDS FIXING~ value missing **")
            return
        else:
            print("~~~ im stuck here ~~")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
