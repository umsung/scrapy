
class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.path = {}

    def go(self, description):
        return self.path.get(description, None)

    def add_paths(self, paths):
        self.path.update(paths)

