class HTMLBaseType():

    def __init__(self, data=None):
        if data:
            if not self.is_type(data):
                raise ValueError()

    def is_type(self, other):
        return type(other) is BaseType

#Types:
#   -Text
#   -List
#   -Dict
#   -Image
#   -Script
#   -Color
#   -Number
#   -URI
class HTMLText(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._text=data

    def is_type(self, other):
        return type(other) is str or type(other) is HTMLText

class HTMLList(HTMLBaseType):

    def __init__(self, data=[]):
        super(data=data)
        self._list=data

    def is_type(self, other):
        return type(other) is list or type(other) is HTMLText

    def insert(self, value):
        self._list.append(value)
        return True

    def insert_list(self, other):
        if self.is_type(other):
            self._list.extend(other)
            return True
        return False

    def __getitem__(self, key):
        return self._list[key]

    def __iter__(self):
        for x in self._list:
            yield x

    def remove(self, obj):
        if obj in self._list:
            self._list.remove(obj)

    def del(self, key):
        if not type(key) is int:
            raise ValueError()
        del self._list[key]

    def pop(self, key=0):
        if not type(key) is int:
            raise ValueError()
        return self._list.pop(key)

class HTMLDict(HTMLBaseType):

    def __init__(self, data={}):
        super(data=data)
        self._dict=data

    def is_type(self, other):
        return type(other) is dict or type(other) is HTMLDict

class HTMLImage(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._src=data

    def is_type(self, other):
        return type(other) is str or type(other) is HTMLImage

class HTMLScript(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._script=data

    def is_type(self, other):
        return type(other) is str or type(other) is HTMLScript

class HTMLColor(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._color=data

    def is_type(self, other):
        return type(other) is str or type(other) is HTMLColor

class HTMLNumber(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._num=data

    def is_type(self, other):
        return type(other) is int or type(other) is HTMLNumber

class HTMLURI(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._uri=data

    def is_type(self, other):
        return type(other) is str or type(other) is HTMLURI
