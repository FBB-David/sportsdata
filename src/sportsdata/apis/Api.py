from enum import Enum
from inspect import isclass

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

import logging
import json
from pandas import DataFrame


################################
# Decorators for the NBA Class #
################################
def clean_inputs(func):
    """
    Iterates over a function's parameters checking for Enum, if one is found, the value is used instead

    Args:
        func: Underlying function to be wrapped

    Returns: Wrapped function

    """

    def new_func(*args, **kwargs):
        cleaned_args = []
        for i in range(len(args)):
            if isclass(type(args[i])) and issubclass(type(args[i]), Enum):
                clean_arg = args[i].value
                cleaned_args.append(clean_arg)
            else:
                cleaned_args.append(args[i])

        for key, val in kwargs.items():
            if isclass(type(val)) and issubclass(type(val), Enum):
                kwargs[key] = val.value

        data = func(*cleaned_args, **kwargs)
        return data

    return new_func


class Api:
    def __init__(self):
        # Get a logger
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
        self.logger = logging.getLogger('sportsdata')

        self.parameters = {}
        for param in self.specs['parameters']:
            self.parameters[param['name']] = {
                'default': param['default'],
                'values': param['values']
            }

    @staticmethod
    def _get_row_set(rs):
        data = []
        for row in rs['rowSet']:
            data_point = dict(zip([h.lower() for h in rs['headers']], row))
            data.append(data_point)
        return data

    @staticmethod
    def _get_data_frames(response, rename_to={}):
        """
        Parse the response for any results and load them into data frames
        Args:
            response:
            rename_to:

        Returns:
            All Result Sets Found as Data Frames

        """
        frames = {}
        info = json.loads(response.text)
        result_sets = info['resultSets']
        for rs in result_sets:
            rs_name = rs['name']
            if rs_name in rename_to.keys():
                rs_name = rename_to[rs_name]

            frames[rs_name] = DataFrame(rs['rowSet'], columns=rs['headers'])

        # Check if there is only one result, if so no need for a dictionary
        if len(frames) == 1:
            key = next(iter(frames))
            frames = frames[key]

        return frames

    @staticmethod
    def _get_dictionary(response):
        return json.loads(response.text)
