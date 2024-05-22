#!/usr/bin/python3
""" Module for testing the HBNBCommand class """
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """ To test the HBNBCommand Console """

    def test_help(self):
        """ Test the help command. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBcommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF all count create destroy help quit show update\n
"""
        self.assertEqual(s, f.getvalue())

    # Test for quit

    def test_do_quit(self):
        """ Tests the quit command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        # modeling when user types `quit anything`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test case for EOF
    def test_do_EOF(self):
        """ Test the EOF command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        # modelling what happens when user inputes `quit`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
            # modeling when user types `EOF anything`
            msg = f.getvalue()
            self.assertTrue(len(msg) == 1)
            self.assertEqual("\n", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
            # modlling when user types `EOF anything`
            msg = f.getvalue()
            self.assertTrue(len(msg) == 1)
            self.assertEqual("\n", msg)

    # Test cases for emptylines
    def test_do_emptyline(self):
        """ Test the Emptyline command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBcommand().onecmd("\n")
        # modelling what happens when user does not type anything
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout'. new=StringIO()) as f:
            HBNBCommand().onecmd("                    \n")
            # modeling when user types lots of whitespaces and hits enter
            msg = f.getvalue()
            self.assertTrue(len(msg) == 0)
            self.assertEqual("", msg)

    # Test cases for do_all
    def test_do_all(self):
        """ Test the do_all command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

    # Test case for do_count present
    # Test case for do_show present
    # Test case for do_create present
    # Test case for do_update present
    # Test case for do_destroy present


if __name__ == "__main__":
    unittest.main()
