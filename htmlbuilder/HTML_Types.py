import rfc3987

class HTMLBaseType():

    def __init__(self, data=None):
        if data:
            if not self.is_type(data):
                raise ValueError()

    @classmethod
    def is_type(cls, other):
        return isinstance(other, HTMLBaseType)

    def _value(self):
        pass

    def _set_value(self, newvalue):
        pass

    @property
    def value(self):
        return self._value()

    @value.setter
    def value(self, newvalue)
        self._set_value(newvalue)

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
        self._set_value(data)

    def _value(self):
        return self._text

    def _set_value(self, newvalue):
        if isinstance(newvalue, HTMLText):
            self._text=newvalue.value
        elif type(newvalue) is str:
            self._text=newvalue
        else:
            raise ValueError()

    @classmethod
    def is_type(cls, other):
        return type(other) is str or isinstance(other, HTMLText)

class HTMLBool(HTMLBaseType):

    def __init__(self, data=False):
        super(data=data)
        self._set_value(data)

    def _value(self):
        return self._bool

    def _set_value(self, value):
        if isinstance(value, HTMLBool):
            self._bool=value.value
        elif type(value) is bool:
            self._bool=value
        else:
            raise ValueError()

    @classmethod
    def is_type(cls, other):
        return type(other) is bool or isinstance(other, HTMLBool)

class HTMLList(HTMLBaseType):

    def __init__(self, data=[], validTypes=[]):
        super(data=data)
        self._validTypes=validTypes
        self._set_value(data)


    def _value(self):
        return self._list

    def _set_value(self, value):
        if isinstance(value, HTMLList):
            if self.validList(value.value)
            self._list=value.value
        elif type(value) is list:
            if self.validList(value):
                self._list=value
            else:
                raise ValueError()
        else:
            raise ValueError()

    @classmethod
    def is_type(cls, other):
        return type(other) is list or  isinstance(other, HTMLList)

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

    def validItem(self, item):
        if self._validTypes:
            if type(item) not in self._validTypes:
                return False
        return True

    def validList(self, l):
        if self._validTypes:
            for i in l:
                if not self.validItem(i):
                    return False
        return True

class HTMLDict(HTMLBaseType):

    def __init__(self, data={}):
        super(data=data)
        self._dict=data

    def _value(self):
        return self._dict

    def _set_value(self, newvalue):
        if HTMLDict.is_type(newvalue):
            self._dict=newvalue

    @classmethod
    def is_type(cls, other):
        return type(other) is dict or isinstance(other, HTMLDict)

class HTMLColor(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._color=data

    def _value(self):
        return self._color

    def _set_value(self, newvalue):
        if HTMLColor.is_type(newvalue):
            self._color=newvalue

    @classmethod
    def is_type(cls, other):
        return type(other) is str or isinstance(other, HTMLColor)

class HTMLNumber(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._set_value(data)

    def _value(self):
        return self._num

    def _set_value(self, newvalue):
        if HTMLNumber.is_type(newvalue):
            if isinstance(newvalue, HTMLNumber):
                self._num=newvalue.value
            else:
                self._num=newvalue

    @classmethod
    def is_type(cls, other):
        return type(other) is int or isinstance(other, HTMLNumber)

class HTMLFeatureOrigin(HTMLList):
    valid_origins=['*', 'self', 'src', 'none']
    def __init__(self, origins=[]):
        
        super(HTMLList)

def __init__(self, data=[], validTypes=[]):
    super(data=data)
    self._validTypes=validTypes
    self._set_value(data)


class HTMLFeatureDirective(HTMLText):


class HTMLFeaturePolicy(HTMLBaseType):
    valid_origins=['*', 'self', 'src', 'none']
    valid_directives=['autoplay', 'camera','document-domain','encrypted-media','fullscreen','geolocation','microphone','midi','payment','vr']
    def __init__(self, directive='', allowlist=[]):
        super(data=allowlist)
        if not HTMLFeaturePolicy.validDirective(directive):
            raise ValueError()
        self._directive=directive
        self._allowlist=allowlist

    def _set_value(self, newvalue):
        if HTMLFeaturePolicy.is_type(newvalue):
            self._list=newvalue

    @property
    def directive(self):
        return self._directive

    @directive.setter
    def directive(self, directive):
        if HTMLFeaturePolicy.validDirective(directive):
            self._directive=directive

    def _value(self):
        return self._directive, self._allowlist

    def _set_value(self, newvalue):
        if HTMLFeaturePolicy.is_type(newvalue):
            if isinstance(newvalue, HTMLList):
                self._allowlist=list(newvalue.value)
            else:
                self._allowlist=newvalue

    @classmethod
    def validDirective(self, directive):
        if directive in HTMLFeaturePolicy.valid_directives:
            return True
        return False

    @classmethod
    def validAllowList(self, allowlist):
        if not self.is_type(allowlist):
            raise ValueError()
        for origin in allowlist:
            if not origin in HTMLFeaturePolicy.valid_origins or rfc3987.match(origin, rule='URI'):
                return False
        return True

    @classmethod
    def is_type(cls, other):
        return ( type(other) is str and HTMLFeaturePolicy.validAllowList(other) ) or isinstance(other, HTMLList)

class HTMLURI(HTMLBaseType):

    def __init__(self, data=''):
        super(data=data)
        self._uri=data

    def _value(self):
        return self._uri

    def _set_value(self, newvalue):
        if HTMLURI.is_type(newvalue):
            self._uri=newvalue

    @classmethod
    def is_type(cls, other):
        if type(other) is str:
            return rfc3987.match(other, rule='URI')
        else:
            return isinstance(other, HTMLURI)
