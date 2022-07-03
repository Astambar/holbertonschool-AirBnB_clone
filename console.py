#!/usr/bin/python3
"""
Creation of the console of the web application
"""

import cmd
from models.base_model import BaseModel
import global_usage
from global_usage import *
from models import storage
import models
import shlex
#print(global_usage.classes)
#print(global_usage)
print(global_usage.City)


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """
        The do_EOF function is called when the user enters EOF (End of File).
        This function is used to exit out of the program.
        
        
        :param self: Access variables that belongs to the class
        :param line: Pass in the line entered by the user
        :return: The string &quot;return&quot;
        :doc-author: Trelent
        """
        print()
        return True

    def do_quit(self, line):
        """
        The do_quit function is called when the user enters the 'quit' command.
        It prints a message and then terminates the program.
        
        :param self: Access variables that belongs to the class
        :param line: Pass the command entered by the user
        :return: The boolean value true
        :doc-author: Trelent
        """
        
        return True

    def do_create(self, className):
        """
        The do_create function creates a new instance of the specified class.
        It then saves it to the JSON file and prints out the id number of the newly created object.
        
        :param self: Reference the attributes and methods of the class in which it is called
        :param className: Create a new instance of the class
        :return: The id of the newly created instance
        :doc-author: Trelent
        """
        
        if not className:
            print("** class name missing **")
        try:
            newClass = eval(className)()
            print(newClass.id)
            newClass.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        The do_show function shows an instance of a class based on the class name and id.
        
        
        :param self: Access the attributes and methods of the class
        :param line: Store the user input
        :return: The object attributes and values
        :doc-author: Trelent
        """
        if line in ["",None]:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{words[0]}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
    def do_destroy(self, line):
        """
        The do_destroy function deletes an instance based on the class name and id.
        
        
        :param self: Reference the class itself
        :param line: Pass the command line arguments to the function
        :return: True if the destroy command is executed successfully
        :doc-author: Trelent
        """
        if not line:
            print("** class name missing ** ")
            return False
        data = shlex.split(line)
        print(data)
        if data[0] not in global_usage.classe:
            print("** class doesn't exist **")
            return False
        if len(data) == 1:
            print("** instance id missing **")
            return False
        classNameId = f"{data[0]}.{data[1]}"
        if classNameId not in models.storage.all():
            print("** no instance found **")
            return False
        del models.storage.all()[classNameId]
        models.storage.save()

    def do_all(self, line):
        """
        The do_all function prints all the objects in storage.
        
        
        :param self: Reference the class itself
        :param line: Pass the command line arguments to the do_all function
        :return: A list of all the objects in storage
        :doc-author: Trelent
        """
        
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                list_item = [str(obj) for key, obj in storage.all().items()
                     if type(obj).__name__ == words[0]]
                print(list_item)
        else:
            list_item = [str(obj) for key, obj in storage.all().items()]
            print(list_item)
    
    def do_update(self, line):
        """
        The do_update function updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        
        
        :param self: Access to the class attributes and methods
        :param line: Pass the line entered by the user
        :return: The value that the setattr function returns
        :doc-author: Trelent
        """
        print(line)
        if not line:
            print("** class name missing ** ")
            return False
        data = shlex.split(line)
        print(data)
        if data[0] not in global_usage.classe:
            print("** class doesn't exist **")
            return False
        lendata = len(data)
        if lendata == 1:
            print("** instance id missing **")
        else:
            strLine = f"{data[0]}.{data[1]}"
            if strLine not in models.storage.all():
                print("** no instance found **")
                return False
            if lendata == 2:
                print("** attribute name missing **")
                return False
            if lendata == 3:
                print("** value missing **")
                return False
        setattr(models.storage.all()[strLine], data[2], data[3])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()