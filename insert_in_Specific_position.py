# Node class definition for a linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a node at a specified position
def insertPos(head, pos, data):
    if pos < 1:
        print("Invalid position!")
        return head

    # Special case for inserting at the head
    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node

    # Traverse the list to find the node before 
    # the insertion point
    prev = head
    count = 1
    while count < pos - 1 and prev is not None:
        prev = prev.next
        count += 1

    # If position is greater than the number of nodes
    if prev is None:
        print("Invalid position!")
        return head

    # Insert the new node at the specified position
    new_node = Node(data)
    new_node.next = prev.next
    prev.next = new_node

    return head

# Driver code to test the insertPos function
if __name__ == "__main__":
    # Initially creating a linked list: 1 -> 2 -> 4
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)

    # Display the original linked list
    print("Original linked list:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    # Insert a new node with value 3 at position 3
    head = insertPos(head, 3, 3)

    # Display the updated linked list
    print("\nLinked list after inserting 3 at position 3:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
