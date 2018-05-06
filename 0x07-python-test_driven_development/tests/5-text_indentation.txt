# run test with python3 -m doctest -v ./tests/5-text_indentation.txt

First import method to test
>>> text_indentation = __import__('5-text_indentation').text_indentation

SUCCESS CASES:

Test string:
     >>> text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
     ... Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
     ... Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud""")
     Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     <BLANKLINE>
     Quonam modo?
     <BLANKLINE>
     Utrum igitur tibi litteram videor an totas paginas commovere?
     <BLANKLINE>
     Non autem hoc:
     <BLANKLINE>
     igitur ne illud quidem.
     <BLANKLINE>
     Fortasse id optimum, sed ubi illud

Test string with extra spaces (shouldn't print spaces at beginning or end of lines):
     >>> text_indentation("   A B.     C D?      E F:     G H     ")
     A B.
     <BLANKLINE>
     C D?
     <BLANKLINE>
     E F:
     <BLANKLINE>
     G H

     >>> text_indentation("   Hey     \n     .     ")
     Hey
     .
     <BLANKLINE>

     >>> text_indentation("      Hello      ")
     Hello

     >>> text_indentation("    ")

FAIL CASES:

Test other data types:
     >>> text_indentation(-1)
     Traceback (most recent call last):
     ...
     TypeError: text must be a string
