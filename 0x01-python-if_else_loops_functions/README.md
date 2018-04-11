## Python - if/else, loops, functions
> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to the Python programming language: if/elif/else loops, range, ord(), chr(),
>  modulo, copy of string, bytecode

### Description of what each file shows:
* Files that start with: (all python scripts execpt #13)
0. print whether the random number is positive or negative
1. print the last digit of the number stored in prints the alphabet, in lowercase, not followed by a new linvariable
2. prints the alphabet, in lowercase, not followed by a new line
3. prints the alphabet, in lowercase, not followed by a new line
4. prints all numbers from 0 to 98 in decimal and in hexadecimal
5. prints numbers from 0 to 99
6. prints all possible different combinations of two digits
7. function that checks for lowercase character
9. function that prints the last digit of a number
10. function that print a string in uppercase followed by a new line
91. function that computes a to the power of b and return the value
12. function that prints the numbers from 1 to 100 separated by a space - FizzBuzz
13. function in C that inserts a number into a sorted singly linked list
100. prints the alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line
101. function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”)
102. Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
### Environment
* Language: Python 3.4.3 (and C for #13)
* OS: Ubuntu 14.04 LTS
* Compiler: python3 (and gcc 4.8.4)
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) [Betty style](https://github.com/holbertonschool/Betty/wiki)
---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)
