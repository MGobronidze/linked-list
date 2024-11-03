# Node class to create linked list nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Python function to delete a node at a specific position
def delete_at_position(head, position):
    # If the list is empty or the position is invalid
    if head is None or position < 1:
        return head

    # If the head needs to be deleted
    if position == 1:
        temp = head
        head = head.next
        temp = None
        return head

    # Traverse to the node before the position to be deleted
    current = head
    for i in range(1, position - 1):
        if current is not None:
            current = current.next

    # If the position is out of range
    if current is None or current.next is None:
        return head

    # Store the node to be deleted
    temp = current.next

    # Update the links to bypass the node to be deleted
    current.next = current.next.next

    # Delete the node
    temp = None
    return head


# Function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Test the delete_at_position function
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print("Original list:")
    printList(head)

    # Deleting the node at position 2
    position = 2
    head = delete_at_position(head, position)

    print(f"\nList after deleting node at position {position}:")
    printList(head)
