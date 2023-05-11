from treeNode import *

# Class for the Tree object that contains a list of TreeNodes and makes a root node. 
class Tree(object): 
    def __init__(self) -> None:
        self._treeNodes: list[TreeNode] = []
        self._root: TreeNode

    # Initiates a Tree
    def startTree(self, games: list[Game]):
        self._root = TreeNode(games, games[0].opening)

    # Recursively generates a tree with depth n. 
    def getNMoves(self, n: int):
        node = self._root
        self.recursiveGetMoves(node, n)

    # Recursive function
    def recursiveGetMoves(self, node: TreeNode, n: int):
            self._treeNodes.append(node)
            c: list[TreeNode] = node.makeChildren()
            if c[0].index <= n:
                for cc in c:
                    self.recursiveGetMoves(cc, n)
