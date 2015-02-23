# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = 2


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(num):
    """Cube a number.

    Args:
        num (int): A number to cube.

    Returns:
        int: The number raised to the third power.

    Examples:
        >>> cube(5)
        125
        >>> cube(-2)
        -8
        >>> cube(0.5)
        0.125
    """

    return num**3

def factorial(num):
    """Compute the factorial of a positive integer.

    Args:
        num (int): A number to compute the factorial for.

    Returns:
        int: The product of all natural numbers less than or equal to the input.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: factorial - input must be positive
        >>> factorial(2.5)
        Traceback (most recent call last):
            ...
        ValueError: factorial - input must be an integer
    """

    if num < 0:
        raise ValueError, "factorial - input must be positive"
    if not isinstance(num, (int, long)):
        raise ValueError, "factorial - input must be an integer"

    res = 1
    for i in range(1, num + 1):
        res *= i

    return res

def count_pattern(pattern, lst):
    """Count occurrences of a pattern in a list.

    Args:
        pattern (list of str): A pattern of symbols to search for.
        lst (list of str): A list of symbols.

    Returns:
        int: The number of times the pattern of symbols appears in the list.

    Examples:
        >>> count_pattern(\
                ('a', 'b'),\
                ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')\
            )
        2
        >>> count_pattern(\
                ('a', 'b', 'a'),\
                ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')\
            )
        3
    """

    plen = len(pattern)
    count = 0

    for i in range(0, len(lst)):
        if lst[i:i + plen] == pattern:
            count += 1

    return count

# Problem 2.2: Expression depth

def depth(expr):
    """Compute the depth of an expression.

    Args:
        expr (str | list of <expr>): A list with elements which are each either
            strings or expressions themselves.

    Returns:
        int: The maximum depth of nested S-expressions.

    Examples:
        >>> depth('x')
        0
        >>> depth(('expt', 'x', 2))
        1
        >>> depth(('+', ('expt', 'x', 2), ('expt', 'y', 2)))
        2
        >>> depth((\
                '/',\
                ('expt', 'x', 5),\
                ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2))\
            ))
        4
    """
    res = 0

    if isinstance(expr, (list, tuple)):
        for sub in expr:
            res = max(res, depth(sub))
        res += 1

    return res

# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    """Access an element in a tree.

    Args:
        tree (int | list of <tree>): A tree represented as nested lists of lists
        index (list of int): A list containing indices for each level of the
            tree leading to the target node.

    Return:
        <tree>: The subtree or leaf found by following the indices.

    Examples:
        >>> tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
        >>> tree_ref(tree, (3, 1))
        9
        >>> tree_ref(tree, (1,1,1))
        6
        >>> tree_ref(tree, (0,))
        ((1, 2), 3)
    """
    res = tree
    for i in index:
        res = res[i]
    return res


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = "N/A"

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = "N/A"

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = "N/A"

# How many hours did this lab take?
HOURS = "1"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
