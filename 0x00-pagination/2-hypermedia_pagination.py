#!/usr/bin/env python3
""" This is a module that implement a get_hyper method that takes the same
arguments (and defaults) as get_page and returns a dictionary containing the
following key-value pairs:
"""


import csv
import math
from typing import List, Optional, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """ This function return a tuple size two containing a start index and
            an end index
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ This is a method that takes two integer arguments page with
            default value 1 and page_size with default value 10
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        elif end_index >= len(dataset):
            return dataset[start_index:]
        else:
            return dataset[start_index:end_index]

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10
            ) -> Dict[str, Optional[int]]:
        """ This return a dictionary containing the key-value pairs """
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
