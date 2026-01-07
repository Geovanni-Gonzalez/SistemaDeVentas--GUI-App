import os

class Repository:
    def __init__(self, filename):
        self.filename = os.path.join("data", filename)
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass

    def save_all(self, items):
        """Save a list of objects to file. Objects must implement to_string()"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(item.to_string() + "\n")

    def load_all(self, mapper_func):
        """Load all lines and map them to objects using mapper_func(line)"""
        items = []
        if not os.path.exists(self.filename):
            return items
            
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    items.append(mapper_func(line))
        return items

    def append(self, item):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(item.to_string() + "\n")
