
def binaryTreePaths(root):
    """Given root node of a BST, return all paths of root to leaf paths"""

    if root is None:
        return []
    
    results = []
    
    dfs(root, "", results)
    return results


def dfs(root, path, results):
    """If no left or right nodes, append this node's val and return, if there
    are still left or right nodes, recurse and pass along another arrow"""
    
    if not root.left and not root.right:
        results.append(path+str(root.val))
        
    if root.left:
        dfs(root.left, path+str(root.val)+"->", results)
        
    if root.right:
        dfs(root.right, path+str(root.val)+"->", results)
    