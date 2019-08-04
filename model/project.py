



class Project:
    def __init__(self, id=None, name=None, description=None, status=None, view_state=None):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.view_state = view_state


    def __repr__(self):
        return "%s;%s" % (self.name, self.description)

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

    def name_key(self):
        if self.name:
            return self.name
