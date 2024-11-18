# Node class definition for a linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the length of the linked list
def find_length(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length

# Driver code to test the find_length function
if __name__ == "__main__":
    # Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    
    # Finding the length of the linked list
    length = find_length(head)
    print("The length of the linked list is:", length)
