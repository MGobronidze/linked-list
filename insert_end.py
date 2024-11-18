# Node class definition for a linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a node at the end of the linked list
def insert_at_end(head, value):
    # Create a new node with the given value
    new_node = Node(value)

    # If the list is empty, make the new node the head
    if head is None:
        return new_node

    # Traverse the list until the last node is reached
    current = head
    while current.next is not None:
        current = current.next

    # Link the new node to the current last node
    current.next = new_node

    return head

# Driver code to test the insert_at_end function
if __name__ == "__main__":
    # Initially creating an empty linked list
    head = None

    # Insert nodes at the end of the linked list
    head = insert_at_end(head, [1,2])
    head = insert_at_end(head, [3,4,5])
    head = insert_at_end(head, [1,2,3,4])
    head = insert_at_end(head, [1,2,34])

    # Display the updated linked list
    print("Linked list after inserting nodes at the end:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
