# Node class to create linked list nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Python Function to remove the last node of the linked list
def removeLastNode(head):
    # If the list is empty, return None
    if head is None:
        return None

    # If the list has only one node, delete it and return None
    if head.next is None:
        head = None
        return None

    # Find the second last node
    second_last = head
    while second_last.next.next is not None:
        second_last = second_last.next

    # Remove the last node
    second_last.next = None

    # Return the modified list
    return head

# Function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Test the removeLastNode function
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    print("Original list:")
    printList(head)

    # Removing the last node
    head = removeLastNode(head)

    print("\nList after removing the last node:")
    printList(head)
