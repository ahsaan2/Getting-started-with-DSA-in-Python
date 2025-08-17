# Creating a node in single LL
# A node contains a value and next pointer
# A node is an object in python, stored at the random locations in memory
# Python lists are dynamic arrays
# [Data, Next] -> [Data, Next] -> [Data, None]

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        # initially we don't have the next


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node1.next = node2
# node2.next = node3
# # node3.next = n
# print(node1)  # since it's an object, it will give us an address here
# print(node1.value)
# print(node2.value)
# # iterate over the LL
# temp = node1
# # while temp is not None:
# while temp:
#     print(temp.value)
#
#     temp = temp.next
#

# Singly-Linked-List
class SingleLinkedList(object):
    def __init__(self):  # self is the current instance of the class
        # initially we don't have any node
        self.head = None  # In python, you can dynamically add attributes to objects
        # create or update the attribute head for this object

    # add nodes
    def append(self, value):
        # create a new node
        new_node = Node(value)
        # is the ll empty
        if self.head is None:
            self.head = new_node
            return
        else:
            # we have some nodes present, and we need to add the new_node
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # Traversal for the LL
    def traversal(self) -> None:
        if self.head is None:
            print("List is empty")
            # return
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" ")
                current = current.next
            # return
    # Insert at specific position
    #(position, insert_Item)
    def insertatposition(self, position, value) -> None:
        # insert at head
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

        # at specific position
        else:
            # [1, 2,[],3, 4, 5 ]
            current = self.head
            prev = current
            while current is not None and position > 0:
                prev = current   #1
                current = current.next   # 2
                position -= 1  # current = 3
            new_node = Node(value)
            prev.next = new_node
            new_node.next = current







# creating an object
sll = SingleLinkedList()
sll.traversal()
sll.append(1)
# sll.traversal()
sll.append(2)
sll.append(3)
sll.append(4)
# sll.append(5)
# sll.append(6)
sll.insertatposition(2, 5)
sll.insertatposition(0, 6)
sll.traversal()
