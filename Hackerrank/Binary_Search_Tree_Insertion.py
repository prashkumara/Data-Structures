def insert(self, val):
    # Enter you code here.
    root = self.root

    if root == None:
        self.root = Node(val)
    else:
        self.Rec_insertion(root, val)
    return root


def Rec_insertion(self, curr_node, val):
    if curr_node.info > val:
        if curr_node.left == None:
            curr_node.left = Node(val)
        else:
            self.Rec_insertion(curr_node.left, val)
    elif curr_node.info < val:
        if curr_node.right == None:
            curr_node.right = Node(val)
        else:
            self.Rec_insertion(curr_node.right, val)
    else:
        print("value already exist")