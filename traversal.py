# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as None

# Python Function to traverse and print the elements of the linked list
def traverse_linked_list(head):
    # Start from the head of the linked list
    current = head

    # Traverse the linked list until reaching the end (None)
    while current is not None:
        # Print the data of the current node followed by a space
        print(current.data, end=' ')
        # Move to the next node
        current = current.next
    print()  # Print a new line after traversing the linked list

# Driver code
if __name__ == "__main__":
    # Create nodes
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # Link nodes
    head.next = second
    second.next = third
    third.next = fourth

    # Traverse and print the linked list
    traverse_linked_list(head)
