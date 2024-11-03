# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as None

# Python function to search for a value in the Linked List
def search_linked_list(head, target):
    # Traverse the Linked List
    while head is not None:
        # Check if the current node's data matches the target value
        if head.data == target:
            return True  # Value found
        # Move to the next node
        head = head.next
    return False  # Value not found

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

    # Target value to search for
    target = 3

    # Search for the target value in the linked list
    if search_linked_list(head, target):
        print(f"Value {target} found in the linked list.")
    else:
        print(f"Value {target} not found in the linked list.")
