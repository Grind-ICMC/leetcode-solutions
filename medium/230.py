# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def percorrer_arvore(self, pointer, k):
        if pointer == None: 
            return
        
        self.percorrer_arvore(pointer.left, k)

        self.contador += 1
        if self.contador == k:
            self.resultado = pointer.val
            return
        
        self.percorrer_arvore(pointer.right, k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.contador = 0
        self.resultado = None

        self.percorrer_arvore(root, k)

        return self.resultado
