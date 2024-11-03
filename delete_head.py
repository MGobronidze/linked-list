# Node class definition for a linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to remove the first node of the linked list
def removeFirstNode(head):
    # Check if the head is None (empty list)
    if not head:
        return None
    
    # Store the current head in a temporary variable
    temp = head
    
    # Move the head pointer to the next node
    head = head.next
    
    # Delete the temporary node
    temp = None
    
    # Return the new head of the linked list
    return head

# Driver code to test the removeFirstNode function
if __name__ == "__main__":
    # Initially creating a linked list: 1 -> 2 -> 3 -> 4
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    # Display the original linked list
    print("Original linked list:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    # Remove the first node
    head = removeFirstNode(head)

    # Display the updated linked list
    print("\nLinked list after removing the first node:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
