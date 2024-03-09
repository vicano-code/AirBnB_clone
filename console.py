#!/usr/bin/python3
"""
 contains the entry point of the command interpreter
"""

import cmd
import sys
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    -Command interpreter for the AirBnB console
    -Accepts commands via interactive mode & non-interactive mode
    """
    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"}

    def emptyline(self):
        '''overide default of running last command when prompt cmd is empty'''
        return

    def do_quit(self, line):
        '''Quits the command interpreter\n'''
        return True

    def do_EOF(self, line):
        '''exit program on EOF command - Ctrl-D(linux), Ctrl-Z(Windows)'''
        print()
        return True

    def do_create(self, line):
        '''
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        '''
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        '''
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234
        '''
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = "{}.{}".format(args[0], args[1])
            if obj_id not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[obj_id])

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id.
        Save the change into the JSON file.
        Ex: $ destroy BaseModel 1234-1234-1234
        '''
        if len(line) == 0:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = "{}.{}".format(args[0], args[1])
            if obj_id not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[obj_id]
                storage.save()

    def do_all(self, line):
        '''
        Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all
        '''
        args = shlex.split(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, obj in storage.all().items():
                if args[0] in key:
                    obj_list.append(obj)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        '''
        if len(line) == 0:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = "{}.{}".format(args[0], args[1])
            if obj_id not in storage.all().keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                '''cast = type(eval(args[3]))'''
                arg3 = args[3]
                arg3 = arg3.strip('"')
                arg3 = arg3.strip("'")
                setattr(storage.all()[obj_key], args[2], arg3)
                storage.all()[obj_key].save()

    def default(self, line):
        '''retrieve all instances of a class using <class name>.all()'''
        match = re.search(r"all()", line)
        if match:
            for cls_name in self.classes:
                if line == "{}.all()".format(cls_name):
                    self.do_all(cls_name)
                    return

        '''retrieve # of instances of a class using <class name>.count()'''
        match = re.search(r"count()", line)
        if match:
            cls_name = line.split('.')[0]
            if cls_name in HBNBCommand.classes:
                obj_count = 0
                for key in storage.all().keys():
                    if cls_name in key:
                        obj_count += 1
                print("{}".format(obj_count))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
