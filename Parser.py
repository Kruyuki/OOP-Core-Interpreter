
# node with necessary fields for parse tree
class Node:

    # creates the tree
    def __init__(self, type, alt, name = None):
        self.parent = None
        self.child = []
        self.alt = alt
        self.type = type
        self.name = name

    # adds child to the node
    def addChild(self, type, alt, name = None):
        self.child.append(Node(type, alt, name))
        self.child[-1].parent = self


class Assign:
    pass

class Prog:
    def parse():
        pass

class Decl_seq:
    def __init__(self, altNo, decl, declSeq):
        self.altNo = altNo
        self.decl = decl
        self.declSeq

    def parse(self):
        self.decl.parse()
        if 





