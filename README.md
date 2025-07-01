Implement a class SortedCircularLinkedList that maintains elements in sorted order on each insertion.

Example: Insert the following integers into the list in this order: 7, 3, 9, 1, 4.

The list should organize itself automatically to remain sorted after each insertion:
After inserting 7: [7]
After inserting 3: [3] -> [7]
After inserting 9: [3] -> [7] -> [9]
After inserting 1: [1] -> [3] -> [7] -> [9]
After inserting 4: [1] -> [3] -> [4] -> [7] -> [9]

Each node's next pointer should continue in sorted order, and the last node should point back to the head to preserve the circular structure.

Your implementation should support:
An insert method
full cycle
A method 
