from .HTML_Types import *

class HTMLAttribute():

    def __init__(self):
        pass

    def _str(self):
        return ''

    def __repr__(self):
        return self.to_str()

class AttributeList(HTMLAttribute, HTMLList):
    def __init__(self, value=[]):
        if super(HTMLList, self).is_type(value):
            super(HTMLList, self).__init__(value)
        elif HTMLText.is_type(value):
            super(HTMLList, self).__init__()
            self.insert(value=value)
        else:
            raise ValueError()

    def insert(self, value):
        if HTMLText.is_type(value):
            return super(HTMLList, self).insert(value)
        return False

    def _str(self):
        return super(HTMLAttribute, self)._str()

class ID_Attribute(HTMLAttribute, HTMLText):

    def __init__(self, id=''):
        super(HTMLText, self).__init__(id)

    def _str(self):
        return "id=%s"%self.value

class Class_Attribute(AttributeList):

    def __init__(self, value=[]):
        super(AttributeList, self).__init__(value=value)

    def _str(self):
        if self.value:
            return "class=\"%s\""%' '.join(self.value)
        return super(AttributeList, self)._str()

class Hidden_Attribute(HTMLAttribute, HTMLBool):

    def __init__(self, value=True):
        super(HTMLBool, self).__init__(value)

    def _str(self):
        if self.value:
            return 'hidden'
        return super(HTMLAttribute, self)._str()

class Style_Attribute(HTMLAttribute, HTMLList):

    def __init__(self, value=[]):
        super(AttributeList, self).__init__(value=value)

    def _str(self):
        if self.value:
            return "style=\"%s\""%' '.join(self.value)
        return super(AttributeList, self)._str()

class Accept_Attribute(HTMLAttribute, HTMLList):
    def __init__(self, value=[]):
        super(AttributeList, self).__init__(value=value)

    def _str(self):
        if self.value:
            return "accept=\"%s\""%' '.join(self.value)
        return super(AttributeList, self)._str()

class Accept_Charset_Attribute(HTMLAttribute):
    #Information can be found at https://tools.ietf.org/html/rfc7231#section-5.3.3
    def __init__(self, value=[]):
        super(AttributeList, self).__init__(value=value)

    def _str(self):
        if self.value:
            return "accept-charset=\"%s\""%' '.join(self.value)
        return super(AttributeList, self)._str()

class AccessKey_Attribute(HTMLAttribute, HTMLText):

    def __init__(self, key=''):
            super(HTMLText, self).__init__(key)

    def _str(self):
        return "accesskey=%s"%self.value

class Action_Attribute(HTMLAttribute, HTMLURI):
    def __init__(self, action=''):
        super(HTMLURI, self).__init__(action)

    def _str(self):
        return "action=%s"%self.value

class Allow_Attribute(HTMLAttribute, HTMLList):
    def __init__(self, value=[]):
        if super(HTMLList, self).is_type(value):
            super(HTMLList, self).__init__(value)
        elif
            super(HTMLList, self).__init__()
            self.insert(value=value)
        else:
            raise ValueError()

    def validList(self, value):
        for v in value:
            if HTMLFeaturePolicy.is_type()

    def insert(self, value):
        if HTMLText.is_type(value):
            return super(HTMLList, self).insert(value)
        return False

    def _str(self):
        return super(HTMLAttribute, self)._str()
