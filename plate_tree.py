

class PlateTree():
    root = None
    final_array = []

    def __init__(self, key, value):
        self.root = PlateNode(key, value)

    def add_level(self, node):
        plate_array = node.value
        for i, item in enumerate(plate_array):
            if len(item) > 1:
                plate = list(plate_array)
                plate[i] = list(item[0])
                node.left = PlateNode('', list(plate))
                plate[i] = list(item[1:])
                node.right = PlateNode('', list(plate))
                return

    def create_tree(self, node=None):
        if node is None:
            node = self.root
        if node.left is None:
            for item in node.value:
                if len(item) > 1:
                    self.add_level(node)
                # else:
                    # self.final_array.append(node.value)
        if node.left is not None:
            self.create_tree(node.left)
        if node.right is not None:
            self.create_tree(node.right)

    def get_plates(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            self.get_plates(node.left)
        if node.right is not None:
            self.get_plates(node.right)
        if node.left is None and node.right is None:
            self.final_array.append(node.value)


class PlateNode():
    key = ''
    value = []
    parent = None
    left = None
    right = None

    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
