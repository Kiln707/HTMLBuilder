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

class HTMLDict(HTMLBaseType):

    def __init__(self, data={}):
        super(data=data)
        self._dict=data

    def is_type(self, other):
        return type(other) is dict or type(other) is HTMLDict
