import json
import os


class ContextExitError(Exception):

    def __init__(self, exc, msg, tcb):
        exc_name = str(exc.__name__)
        msg = str(msg)
        super().__init__(f"{exc_name} -> {msg}")


class AttributeHandler:
        
    def __init__(self, json_data):
        self.__dict__ = json_data


    def __repr__(self):
        pair_string_list = [f"{key}={value.__repr__()}" for key, value in self.__dict__.items()]
        pair_string = ", ".join(pair_string_list)
        class_name = self.__class__.__name__
        return f"{class_name}({pair_string})"

    
class MethodHandler:

    def __init__(self, parent):
        self._parent = parent


    def dump(self):
        self._parent._dump()


class JSONHandler:


    def __init__(self, filename, allow_method_handler=False):
        self._filename = filename
        self._json = dict()
        self._allow_method_handler = allow_method_handler

    
    def _load(self):
        # reads JSON file
        with open(self._filename, 'r') as file:
            self._json = json.load(file)


    def _dump(self):
        # writes JSON file
        with open(self._filename, 'w') as file:
            json.dump(self._json, file)


    def __enter__(self):
        
        # if file does not exist, then is created
        if not os.path.isfile(self._filename):
            self._dump()

        self._load()

        if self._allow_method_handler:
            return AttributeHandler(self._json), MethodHandler(self)
        else:
            return AttributeHandler(self._json),


    def __exit__(self, *p):
        if all(p) == False:
            self._dump()
        else:
            raise ContextExitError(*p)



with JSONHandler(filename="data.json") as data:
    data.name = "Quido"
    print(data)