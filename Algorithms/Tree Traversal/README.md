# Tree Traversal Algorithm

Tree Traversal refers to visiting each node present in the tree exactly once, in order to update or check them.

There are three types of tree traversals:
- **In-order traversal** → refers to visiting the left node, followed by the root and then the right nodes.
Here D is the leftmost node where the nearest root is B. The right of root B is E. Now the left sub-tree is completed, so I move towards the root node A and then to node C.
- **Pre-order traversal** → refers to visiting the root node followed by the left nodes and then the right nodes.
In this case, I move to the root node A and then to the left child node B and to the sub child node D. After that I can go to the nodes E and then C.
- **Post-order traversal** → refers to visiting the left nodes followed by the right nodes and then the root node
I go to the most left node which is D and then to the right node E. Then, I can go from the left node B to the right node C. Finally, I move towards the root node A.