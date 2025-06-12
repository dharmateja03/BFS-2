# // Time Complexity :O(N)
# // Space Complexity :O(N)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :no


# // Your code here along with comments explaining your approach
# We can do this with both bfs and dfs we need keep track of parent and level in bfs you dont neeed to track level as for while loop for len of q you will be in same level so checking ap
# parent works fine but in dfs you need to keep track of both

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        #keep track
        q=deque()
        q.append(root)
        while(q):
            t=len(q)
            xFound=False
            yFound=False
            while(t):
                t-=1
                node=q.popleft()
                if node.left and node.right:
                    if node.left.val==x and node.right.val==y:return False
                    if node.left.val==y and node.right.val==x:return False
                if node.val==x:xFound=True
                if node.val==y:yFound=True
                if xFound and yFound:return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False

###########################################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.xPar=None
        self.xle=0
        self.yle=0
        self.yPar=None
        if root and (x==root.val or y==root.val):return False
        def bfs(root,x,y):
            q=deque()
            q.append(root)
            level=0
            while(q):
                le=len(q)
                while(le):
                    node=q.popleft()
                    if node and ((node.left and  node.left.val==x) or (node.right and  node.right.val==x)):
                        self.xPar=node
                        self.xle=level
                    if node and ((node.left and  node.left.val==y) or (node.right and  node.right.val==y)):
                        self.yPar=node
                        self.yle=level
                    if self.xPar and self.yPar: return
                    if node:
                        q.append(node.left)
                        q.append(node.right)
                    le-=1
                level+=1
                    
        
        # def dfs(root,x,y):
        #     if not root:return 
            
                
        #     if (root.left and root.left.val==x )or (root.right and root.right.val==x):
        #         self.xPar=root
                
        #     if (root.left and root.left.val==y)or (root.right and root.right.val==y):
        #         self.yPar=root
        #     l=dfs(root.left, x,y)
            
        #     r=dfs(root.right, x,y)
        bfs(root,x,y)
        # print(self.yPar,"j",self.xPar)
            
        # print(f"bfs vals{bfs(root,x),bfs(root,y)}..dfs{dfs(root,x),dfs(root,y)}")
        return self.xle==self.yle and self.yPar!=self.xPar

        
