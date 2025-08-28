class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        if self.root is None:
            return None

       
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            
            node = nodes_to_visit.pop(0)

           
            if node["id"] == target_id:
                return node

            nodes_to_visit = node.get("children", []) + nodes_to_visit

        return None
