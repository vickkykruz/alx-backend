#!/usr/bin/env python3
""" This is a module that create a function and the function should return a
tuple of size two containing a start index and an end index corresponding to
the range of indexes to return in a list for those particular pagination
parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """ This function return a tuple size two containing a start index and an
        end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
