import os
import sys
import inspect
from dataclasses import dataclass
from typing import Any
import json


@dataclass
class GuardInfo:
    error:Exception = None
    return_value:Any = None
    init_time:Any = None


class Guard:

    def __init__(self, json_filename:str=None):
        self._json_filename = json_filename
        self._json_data = None

        self._return_value = None
        self._error_value = None



    
    def run(self, main_function):

        __name__ = inspect.getmodule(main_function).__name__

        def wrapper(*args, **kwargs):
            if __name__ == "__main__":
                args = {num: value for num, value in enumerate(sys.argv)}
                try:
                    if self._json_filename is not None:
                        self._return_value = main_function(args, self._json_data)
                    else:
                        self._return_value = main_function(args)
                except Exception as exc:
                    self._error_value = exc
                    if self._error_value is not None:
                        print("*Guard exception: ", self._error_value)

                if self._json_filename is not None:
                    with open(self._json_filename, "w") as json_file:
                        json.dump(self._json_data, json_file)

        return wrapper()
        
    
    @property
    def INFO(self):
        guard_info = GuardInfo(
            error = self._error_value,
            return_value = self._return_value
        )
        return guard_info
    

    @property
    def JSON_FILENAME(self):
        return self._json_filename


    @JSON_FILENAME.setter
    def JSON_FILENAME(self, value:str):

        self._json_filename = value

        try:
            with open(self._json_filename ,"r") as json_file:
                self._json_data = json.load(json_file)
        

        except FileNotFoundError as exc:
            json_data = dict()
            with open(self._json_filename, "w") as json_file:
                json.dump(json_data, json_file)

        


Guard = Guard()