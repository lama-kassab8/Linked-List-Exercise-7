class Node:

    def __init__(self, data):
        self.data= data
        self.next= None

class  CircularLinkedList:

    def insert_and_sort(self, head, n):
        new_node= Node(n)
        # if the list is empty, create a list and make it circular
        if head is None:
            new_node.next= new_node
            return new_node
        
        if n < head.data: # if n is the smallest element in the list, to place it at the beginning of the list, do the following:
            current= head
            while current.next != head: # traverse the list to the last node before it points to the head again
                current=current.next
            current.next= new_node # make the last node in the list point to the new node
            new_node.next= head # make the head of the list the second element in it after new_node
            return new_node # now new_node is the new head
        
        if n> head.data: # if n is bigger than the first element in the list, do the following: 
            current= head # start from the head
            while current.next != head and current.next.data < n: # traverse the list to the last node before it points to the head again so long that n is bigger than the value of the last node in the list
                current= current.next
            # insert the new node between current and current.next    
            new_node.next= current.next 
            current.next= new_node
            return head # as head remains untouched
        
    # the following method prints out the sorted list   
    def print_list(self,head):
        if head is None:
            print("The list is empty.")
            return
        current= head
        while True:
            print(current.data, end= ", ")
            current= current.next
            if current is head:
                break
        print(f"back to {head.data}")

# create a CircularLinkedList object
cll = CircularLinkedList()
head = None  # start with an empty list

# insert the elements one at a time and print out the updated list after each insertion
for value in [7, 3, 9, 1, 4]:
    head = cll.insert_and_sort(head, value)
    cll.print_list(head)



        
