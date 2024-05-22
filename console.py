#!/usr/bin/python3
""" This module is the entry point of the command interpreeter """

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.cmd):

    """ This class activates the command interpreeter """

    prompt = "Alx$ "

    def default(self, line):
        """ catch commands, but if command does not match it does nothing"""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """ Intercepts commands to test for the syntax of the class """
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_arg = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                    '^(?:"([^"]*)?(?:, (.*))?$', attr_to_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self. classname, uid, s_dict):
        """ Helper method for update() that has a dictionary. """
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name is missing **")
        elif classname not in storage.classes():
            print("** class does not exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """ Handles the end of file character. """

        print()
        return True

    def do_quit(self, line):
        """exits the console program """

        return True

    def emptyline(self):
        """Does not do anything on enter. """

        pass

    def do_create(self, line):
        """ Creates an instance """

        if line == "" or line is None:
            print("** class name is missing **")
        elif line not in storage.classes():
            print("** class does not exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """ Prints the representation of an instance in string format """

        if line == or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class does not exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(sef, line):
        """ Deletes aninstance based on the name and id of the class """

        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class does not exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ Prints all representation of instances in string format """

        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class does not exist **")
            else:
                nl = [str(obj) for key, obj in storage. all().items()]
                    if type(obj).__name__ == words[0]]
                print(nl)
            else:
                new_list = [str(obj) for key, obj in storage.all().items()]
                print(new_list)

    def do_count(self, line):
        """ Counts the instances of a class """

        words = line.split(' ')
        if not words[0]:
            print("**class name is missing **")
        elif words[0] not in storage.classes():
            print("** class does not exist **")
        else:
            matches = [
                    k for k in storage.all() if k.startswith(
                        words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """ Updates an instance by adding or updating attribute """

        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class does not exist **")
        elif uid is None:
            print("** the id of instance is missing **")
        else:
            key "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** instance is not found **")
            elif not attribute:
                print("** attribute name is missing **")
            elif not value:
                print("** value is missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '"')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass # fine, continues as a string
                    setattr(storage.all()[key], attribute, value)
                    storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
