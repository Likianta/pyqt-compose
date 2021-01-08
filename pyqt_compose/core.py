from .keywords import this, parent


class Context:
    _context = [[]]
    _index = 0
    _node = _context[_index]
    
    def new_layer(self):
        self._context.append([])
        self._index += 1
        self._node = self._context[self._index]  # i.e. -1
        
    def append(self, obj):
        self._node.append(obj)
        
    def backwards(self):
        self._index -= 1
        self._node = self._context[self._index]
        
    def __len__(self):
        return len(self._node)


context = Context()


class Property:
    _deliver: list
    
    def __init__(self):
        pass
    
    def __setattr__(self, key, value):
        self.__dict__[key] = value
        
        if (on_key := f'on_{key}') not in self.__dict__:
            self.__dict__[on_key] = Signal(self._deliver)


class Signal:
    
    def __init__(self, _deliver):
        self.slots = set()
        self._deliver = _deliver
    
    def __call__(self, *args, **kwargs):
        """
        Examples:
            # assume button.clicked is an instance of Signal
            button.clicked()
        """
        for f in self.slots:
            f(*self._deliver, *args, **kwargs)
        
    def binding(self, func):
        """
        Examples:
            # assume button.clicked is an instance of Signal
            button.clicked.binding(lambda : print('button is clicked'))
        """
        self.slots.add(func)


class Compose:
    
    def build(self):
        pass
    
    def __enter__(self):
        context.append(self)
        this.represents(self)
        this.index = len(context)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        parent.represents(self)


class Component(Compose):
    
    def __init__(self, **kwargs):
        self.apply(**kwargs)
    
    def apply(self, width, height):
        pass
    
    def on_completed(self):
        pass


if __name__ == '__main__':
    comp = Component()
