class StaticKeyword:
    
    def __init__(self, text, value):
        self.text = text
        self.value = value


true = StaticKeyword('true', True)
false = StaticKeyword('false', False)
null = StaticKeyword('null', None)


# ------------------------------------------------------------------------------

class DynamicKeyword:
    
    def __init__(self, name):
        self.virtual_ref = name
        self.real_ref = None
    
    def represents(self, obj):
        self.real_ref = obj


class This(DynamicKeyword):
    index: int

    def __init__(self):
        super().__init__('this')
        self.parent = Parent()

    @property
    def siblings(self):
        return self.parent.children
    
    @property
    def last_sibling(self):
        if self.index == 0:
            return None
        else:
            return self.parent.children[self.index - 1]

    @property
    def next_sibling(self):
        if self.index == len(self.parent.children) - 1:
            return None
        else:
            return self.parent.children[self.index + 1]


class Parent(DynamicKeyword):
    
    def __init__(self):
        super().__init__('parent')
        self.children = []


this = This()
parent = this.parent
last_sibling = this.last_sibling
next_sibling = this.next_sibling
siblings = this.siblings


# ------------------------------------------------------------------------------

# noinspection PyPep8Naming
class final:
    
    def __init__(self, value):
        self.value = value
