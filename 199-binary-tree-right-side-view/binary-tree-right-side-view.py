from collections import deque

class Solution:
    def rightSideView(self, root):

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:

            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                # Last node of this level
                if i == size - 1:
                    result.append(node.val)

        return result


        
        