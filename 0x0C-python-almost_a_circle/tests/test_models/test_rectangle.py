#!/usr/bin/python3
"""
Unittest for Rectangle Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""


import os
import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """Pep8 models/rectangle.py & tests/test_models/test_rectangle.py"""
    def test_pep8(self):
        """Pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase(unittest.TestCase):
    """Tests for models/rectangle.py"""

    """Test attributes"""
    def test_all_attr_given(self):
        """Test all attributes match what's given"""
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 20)
        self.assertTrue(r1.x == 1)
        self.assertTrue(r1.y == 2)
        self.assertTrue(r1.id == 99)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        r2 = Rectangle(3, 4)
        self.assertTrue(r2.width == 3)
        self.assertTrue(r2.height == 4)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_attr_validated(self):
        """Test attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 1, 1, 1, 1)
            Rectangle([10, 3], 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {20, }, 1, 1, 1)
            Rectangle(1, {"d": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -20, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -99, 1)

    def test_private_attr_access(self):
        """Test private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    """Test args given"""
    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        """Test too little args given throws error"""
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    """Test class"""
    def test_class(self):
        """Test class created is indeed Rectangle"""
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    """Test methods"""
    def test_area(self):
        """Test method: area"""
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_print(self):
        """Test method: __str__"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_update(self):
        """Test method: update(*args)"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/2')
        r.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (99) 3/4 - 1/2')
        """Test invalid *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -99)
        """Test method: update(*kwargs)"""
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')
        """Test mixture of valid and invalid *kwargs"""
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 770/880 - 990/2')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        rdic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rdic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**rdic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')
