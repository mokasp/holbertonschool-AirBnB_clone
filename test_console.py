#!/usr/bin/python3

import cmd
import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    A class runs the AirB&B Console

    Attributes
    ~~~~~~~~~~
    None (check with Kasper?)

    Methods
    ~~~~~~~
    emptyline():
        Do nothing when an empty line is entered.
    do_quit():
        Exits the program when called by the user
    do_EOF():
        Enter the command "EOF" to quit the program
        Handles "CTRL D"
    do_create():
        Creates a new instance of BaseModel
        Saves the instance to the "file.json"
        Prints instance's ID
    do_show():
        
    
    """

    prompt = "(hbnb) \n"

    def emptyline(self):
        """ Do nothing when an empty line is entered """
        # print("Empty line!")
        pass

    def do_quit(self, line):
        """ Quit command to exit the program """
        # print("Goodbye!")
        return True

    def do_EOF(self, line):
        """
        Enter the command "EOF" to quit the program
        Handles "CTRL D"
        """
        # print("Goodbye! (CTRL+D)")
        return True

    def do_create(self):
        """
        Creates a new instance of BaseModel
        Saves the instance to the "file.json"
        Prints instance's ID
        """
        if not ARG[0]: # if class name is missing
            print("** class name missing **")
        if not arg?: #if class name doesn't exist
            print("** class doesn't exist **")

    def do_show(self):

if __name__ == '__main__':
    HBNBCommand().cmdloop()
