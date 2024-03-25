class MyNewCollection:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        """Return the iterator object (itself in this case)."""
        self.index = 0
        return self
    
    def __next__(self):
        """Return the next item from the collection."""
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def to_list(self):
        """Convert to a list."""
        return list(self.data)
    
    def __len__(self):
        """Return the number of items in the collection."""
        return len(self.data)
    
    def __str__(self) -> str:
        out = ""
        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"    
    
    def __eq__(self, other):
        """Check if two collections instances are equal based on their data."""
        if isinstance(other, MyNewCollection):
            return self.data == other.data
        return False
    
    def __getitem__(self, index):

        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError