import json
import os


class _JSONHandler:

    def __init__(self, filename):
        self._fname = filename
        self._init = False
        self.json = dict()


    def _open_read(self):
        with open(self._fname, 'r') as f:
            self.json = json.load(f)


    def _open_write(self):
        with open(self._fname, 'w') as f:
            json.dump(self.json, f, ensure_ascii=False)


    def load(self):
        try:
            self._open_read()
        except:
            self._open_write()
        self._init = True


    def dump(self):
        if self._init:
            self._open_write()



class AttribBearer:

    def __init__(self, dict_):
        self.__dict__ = dict_

    def __getitem__(self, key):
        return self.__dict__[key]



class JSONContext:

    def __init__(self, *filenames):
        self._handlers = []
        
        for fname in filenames:
            handler = _JSONHandler(fname)
            handler.load()
            self._handlers.append(handler)


    def __enter__(self):
        return tuple([AttribBearer(h.json) for h in self._handlers])


    def __exit__(self, *x):
        for handler in self._handlers:
            handler.dump()



