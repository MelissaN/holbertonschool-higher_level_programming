# run test with python3 -m doctest -v ./tests/3-say_my_name.txt

First import method to test
>>> say_my_name = __import__('3-say_my_name').say_my_name

SUCCESS CASES:

Test two strings given:
     >>> say_my_name("First", "Middle Last")
     My name is First Middle Last

     >>> say_my_name("Melissa")
     My name is Melissa 

FAIL CASES:

Test other data types:
     >>> say_my_name(123, "Last")
     Traceback (most recent call last):
     ...
     TypeError: first_name must be a string

     >>> say_my_name("Melissa", ["Ng", "Hey"])
     Traceback (most recent call last):
     ...
     TypeError: last_name must be a string

Test extra args:
     >>> say_my_name("Melissa", "Ng", "extra")
     Traceback (most recent call last):
     ...
     TypeError: say_my_name() takes from 1 to 2 positional arguments but 3 were given

Test too few args
     >>> say_my_name()
     Traceback (most recent call last):
     ...
     TypeError: say_my_name() missing 1 required positional argument: 'first_name'

     >>> say_my_name(None)
     Traceback (most recent call last):
     ...
     TypeError: first_name must be a string
