# // Time Complexity :O(N)
# // Space Complexity :O(h)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :no


# // Your code here along with comments explaining your approach
# This is can be done with both DFS and BFS , In DFS first we try to get to right most node connected to root directly ,then we make left call.
# In BFS or level order we jsut update temp again and again while we are still in level then update ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #DFS

        def helper(root, level,ans):

            #base
            if not root:return


            #logic
                #add ele to ans and increase length
            if level==len(ans):
                ans.append(root.val)
                
            helper(root.right,level+1,ans)
            helper(root.left,level+1, ans)
        ans=[]
        helper(root, 0,ans)
        return ans


###########################################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # this is bfs/ level order 

        ans=[]

        q=deque() # for level order and to get right ele
        q.append(root)
        if not root:return []

        
        while(len(q)):
            qsize=len(q) # for levels
            temp=-1
            
            while(qsize>0):
                
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    temp=node.val
                qsize-=1
            #we added all our level elements to temp
            if temp!=-1:
                ans.append(temp)
        # mans=[]
        # for i in ans:
        #     mans.append(i[-1])
        return ans


