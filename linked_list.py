from __future__ import unicode_literals


class LinkedList(object):
    """Class for a singly-linked list"""
    def __init__(self, iterable):
        self.length = len(iterable) ##Will resize for pop, insert, remove

        for item in zip(range(self.length, 0, -1), iterable.reverse()):

            #Case: last item
            Node(val)

            #Case middle items
            #Node(val, stored_for_next)

            #Case first item; use None as ptr
            #self.header = Node(val, stored_for_next)
            #

            stored_for_next = # last 



    def insert(val):
        #Will insert val at head of LinkedList
        self.header = Node(val, self.header)
        self.length += 1
        return None

    def pop():
        #Pop the first val off the head and return it
        to_return = self.header
        self.header = to_return.next
        to_return.next = None
        self.length -= 1
        return to_return

    def size(self):
        return self.length

    def search(val):
        #Return the node containing val if present, else None
        node, left = _find(val)
        return node

    def remove(val):
        #Remove given node from list, return None
        node_to_remove = search(val)


    def display():  
        #Will print LinkedList as Tuple literal
        end_flag = False
        vals = []
        current_node = self.header

        while not end_flag:
            vals.append(current_node)
            if current_node.next:
                current_node = current_node.next
            else:
                end_flag = True
                break

        vals = tuple(vals)
        return str(vals)

   def _find(val):
        #Private to return a Node and left-neighboor by val
        val_present = False
        node_inspected = self.header

        while not val_present:
            #Interrogate each Node
            if node_inspected.val = val:
                break
            else:
            #Keeping track of node to left; incrementing node
                node_inspected = left_node
                node_inspected = node_inspected.next

        return node_inspected, left_node


    class Node(object):


        def __init__(self, val, next=None):
            self.val = val
            self.next = next

        def __repr__(self):
            #Code here