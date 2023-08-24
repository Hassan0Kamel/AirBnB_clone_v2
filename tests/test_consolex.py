#!/usr/bin/python3
"""initnsole"""
import sys
import unittest
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """uniole"""

    def test_console_docs(self):
        """chcs"""
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_create(self):
        """teeate"""
        output = StringIO()
        sys.stdout = output

        HBNBCommand().do_create(None)
        self.assertEqual(output.getvalue(), '** class name missing **\n')
        output.close()

        output = StringIO()
        sys.stdout = output
        HBNBCommand().do_create("base")
        self.assertEqual(output.getvalue(), '** class doesn\'t exist **\n')
        output.close()

        output = StringIO()
        sys.stdout = output
        HBNBCommand().do_create("BaseModel")
        self.assertEqual(output.getvalue(), '** class doesn\'t exist **\n')
        output.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
