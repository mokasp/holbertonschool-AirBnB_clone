#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """
    A class that runs the AirB&B Console

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

    def emptyline(self):
        """ Do nothing when an empty line is entered\n"""
        # print("Empty line!")
        pass

    def do_quit(self, line):
        """ Quit command to exit the program\n"""
        # print("Goodbye!")
        return True

    def do_EOF(self, line):
        """
        Enter the command "EOF" to quit the program\n
        Handles "CTRL D\n"
        """
        # print("Goodbye! (CTRL+D)")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
