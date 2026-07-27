from collections import deque

class Solution:
    def findBottomLeftValue(self, root):

        queue = deque([root])

        ans = root.val

        while queue:

            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                if i == 0:
                    ans = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return ans