from .HTML_Types import *

class HTML_Attribute():

    def __init__(self):
        pass

    def to_str(self):
        return ''

    def __repr__(self):
        return self.to_str()

class ID(HTML_Attribute):

    def __init__(self, id=''):
        if id and not type(id) is str:
            raise ValueError()
        self._id=id

    def to_str(self):
        return 'id=%s'%self._id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not type(value) is str:
            raise ValueError()
        self._id = value

class Class(HTML_Attribute, HTMLList):

    def __init__(self, c=[]):
        if self.is_type(c):
            super(c)
        if HTMLText.is_type(c):
            super()
            self.insert(class_id=c)
        else:
            raise ValueError()
