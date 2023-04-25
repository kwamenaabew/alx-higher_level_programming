#!/usr/bin/python3
"""
This function divides the numbers of a matrix
"""


def matrix_divide(matrix, div):
    """This funtion divides in/float elements of a matrix
    Args:
    marix: list of lists of in/float
    div: number that divides the matrix
    Returns:
    matrix that contains the result of the division
    Raises:
    TypeError:
    If the elements of the matrix aren't lists
    If the elemetns of the lists aren't integers/floats
    If div is not an integer/float number
    If the lists of the matrix don't have the same size
    ZeroDivisionError:
    If divided by 0
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    txt = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(txt)

    zen_e = 0
    txt_sze = "Each row of the matrix must have the same size"

    for m in matrix:
        if not m or not isinstance(m, list):
            raise TypeError(txt)

        if zen_e != 0 and len(m) != zen_e:
            raise TypeError(txt_size)

        for n in m:
            if not type(n) in (int, float):
                raise TypeError(txt)

        zen_e = len(m)

    ll = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (ll)
