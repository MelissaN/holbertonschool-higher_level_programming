## Python - import & modules
> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to the Python programming language: importing modules and using definitions, not executing 
> prints when imported, ...

### Description of what each file shows:
Files that start with:
0. imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
1. imports functions from the file calculator_1.py and prints examples of add, sub, mul, div
2. prints the number of and the list of its arguments
3. prints the addition of all arguments (Sample usage: ```./pythonscript 79 -3 10 8```)
4. prints specific content within the compiled module (curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc")
5. imports the variable a from the file variable_load_5.py and prints its value
100. imports all functions from the file calculator_1.py and handles basics operations (Sample usage: ```./100-my_calculator.py 5 / 7 ```)
101. prints #pythoniscool via importing another file that prints it
102. write Python function def magic_calculation(a, b): that does exactly the same as below bytecode:
103. prints the alphabet in uppercase, followed by a new line
```
3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
### Environment
* Language: Python 3.4.3
* OS: Ubuntu 14.04 LTS
* Compiler: python3
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

