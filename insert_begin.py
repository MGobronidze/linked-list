# Node class definition for a linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a new node at the beginning of the linked list
def insert_at_beginning(head, value):
    # Create a new node with the given value
    new_node = Node(value)

    # Set the next pointer of the new node to the current head
    new_node.next = head

    # Move the head to point to the new node
    head = new_node

    # Return the new head of the linked list
    return head

# Driver code to test the insert_at_beginning function
if __name__ == "__main__":
    # Initially creating a linked list: 2 -> 3 -> 4
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)

    # Display the original linked list
    print("Original linked list:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    # Insert a new node with value 1 at the beginning
    head = insert_at_beginning(head, 1)

    # Display the updated linked list
    print("\nUpdated linked list after inserting 1 at the beginning:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
