class TreeNode(object):
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    def search_dfs(self, data):
        to_search = [self]

        while to_search:
            current = to_search.pop()
            if current.data == data:
                return current

            to_search.extend(current.children)

        #If can't find
        return None 

    def search_bfs(self, data):
        to_search = [self]

        while to_search:
            current = to_search.pop(0)
            if current.data == data:
                return current

            to_search.extend(current.children)

        #If can't find
        return None 


class Tree(object):
    def __init__(self, root):
        self.root = root

    def search_dfs(self, data):
        """Start searching from root node, refer to TreeNode class' search"""
        
        return self.root.search_dfs(data)

    def search_bfs(self, data):
        """Start searching from root node, refer to TreeNode class' search
        Find closest one, so Breadth First Search"""
        
        return self.root.search_bfs(data)
