#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 05:43:54 2018
Updated on Wed Apr 25 06:31:00 2018
Updated on Tue May 01 15:57:00 2018
@author: sidharthsuman

Data structures in python
"""
# Linked list

class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None

    def set_next(self,node):
        self.__next = node
        return True

    def set_data(self,data):
        self.__data = data
        return True

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

class Linked_list:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self,data):
        new_node = Node(data)
        if(self.__head == None):
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        if(self.__head == None):
            print('Linked list is empty')
        else:
            temp_node = self.__head
            while(temp_node != None):
                print(temp_node.get_data())
                temp_node = temp_node.get_next()

    def find_node(self,data):
        if(self.__head == None):
            print('Linked list is empty')
            return
        else:
            temp = self.__head
            position = 0
            while(temp!=None):
                position = position + 1
                if(temp.get_data()==data):
                    print('position of the node is: ',position)
                    return(position,temp)
                else:
                    temp = temp.get_next()
            print('Node not in the linked list')
            return

    def delete(self,data):
        if(self.__head==None):
            print('linked list is empty')

        elif(self.__head.get_data() == data):
            if(self.__head == self.__tail):
                self.__head = None
                self.__tail = None
            else:
                temp = self.__head.get_next()
                self.__head = temp
        else:
            temp = self.__head
            temp_previous = self.__head
            while(temp!=None):
                if(temp.get_data()==data):
                    temp_previous.set_next(temp.get_next())
                    temp.set_data(None)
                    return('Node deleted')
                else:
                    temp_previous = temp
                    temp = temp.get_next()

            print('Node not in the linked list')
            return

    def swap_nodes(self,data1,data2):
        temp = self.__head
        prev1 = None
        prev2 = None
        node1 = None
        node2 = None
        prev = None
        while(temp != None):
            if(temp.get_data() == data1):
                node1 = temp
                prev1 = prev
            elif(temp.get_data() == data2):
                node2 = temp
                prev2 = prev
            if(node1 != None and node2 != None):
                break
            prev = temp
            temp = temp.get_next()

        if(node1 == None or node2 == None):
            print('Nodes not found')
            return

        if(prev1 == None and node1 != None and prev2 != None):
            temp = node1.get_next()
            node1.set_next(node2.get_next())
            node2.set_next(temp)
            self.__head = node2
            prev2.set_next(node1)

        elif(prev2 == None and node2 != None and prev1 != None):
            temp = node1.get_next()
            node1.set_next(node2.get_next())
            node2.set_next(temp)
            self.__head = node1
            prev1.set_next(node2)
        else:
            prev1.set_next(node2)
            prev2.set_next(node1)
            temp = node1.get_next()
            node1.set_next(node2.get_next())
            node2.set_next(temp)
        self.display()
        return

    def insert(self,data,data_before):
        new_node = Node(data)
        temp = self.__head
        temp_next = self.__head
        if(data_before == None):
            new_node.set_next(self.__head)
            self.__head = new_node
        else:
            while(temp.get_data() != data_before):
                temp = temp.get_next()
            temp_next = temp.get_next()
            new_node.set_next(temp_next)
            temp.set_next(new_node)
        return

    def get_mid(self):
        temp = self.__head
        slow_node = temp
        while(temp != None):
            temp = temp.get_next()
            temp = temp.get_next()
            slow_node = slow_node.get_next()
        print(slow_node.get_data())

    def print_nth_from_end(self,n):
        ref_node = self.__head
        main_node = self.__head
        i = 0
        while(i<=n):
            i+=1
            ref_node = ref_node.get_next()
        while(ref_node.get_next() != None):
            main_node = main_node.get_next()
            ref_node = ref_node.get_next()
        print(main_node.get_data())
        return

# code to check implementation of linked list

lit = Linked_list()
lit.add(1)
lit.add(2)
lit.add(3)
lit.add(4)
lit.add(5)
print('head',lit.get_head().get_data())
print('tail',lit.get_tail().get_data())
lit.find_node(4)
lit.insert(7,5)
print('displaying')
lit.display()
lit.print_nth_from_end(3)


# Stack

class Stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None] * max_size
        self.__top = -1

    def get_max_size(self):
        return(self.__max_size)

    def is_empty(self):
        if(self.__top == -1):
            return(True)
        return(False)

    def is_full(self):
        if(self.__top == self.__max_size):
            return(True)
        return(False)

    def display(self):
        temp = self.__top
        temp_top = temp
        while(temp>=0):
            print(self.__elements[temp])
            temp -= 1

    def push(self,data):
        if(self.is_full()):
            print('Stack is full')
            return
        else:
            self.__top += 1
            self.__elements[self.__top] = data
            return

    def pop(self):
        if(self.is_empty()):
            print('Stack is empty')
            return
        else:
            popped_data = self.__elements[self.__top]
            self.__elements[self.__top] = None
            self.__top -= 1
            return(popped_data)

'''
# code to check implementation of stack
print('stack')
a = Stack(10)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.display()
print(a.pop())
print(a.get_max_size())
print(a.is_full())
print(a.is_empty())
'''

# Queue

class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if(self.__rear == self.__max_size-1):
            print('Queue is full')
            return(True)
        return(False)

    def is_empty(self):
        if(self.__rear == -1 | self.__front == self.__rear):
            print('Queue is empty')
            return(True)
        return(False)

    def enqueue(self,data):
        if(self.is_full() == True):
            return
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data
            return

    def dequeue(self):
        if(self.is_empty() == True):
            return
        else:
            popped_element = self.__elements[self.__front]
            self.__front += 1
            return(popped_element)

    def display(self):
        if(self.is_empty() == True):
            return
        else:
            temp = self.__front
            while(temp <= self.__rear):
                print(self.__elements[temp])
                temp += 1
        return

'''
# code to check implementation of queue
print('Queue')
a = Queue(5)
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.display()
print(a.is_full())
a.enqueue(6)
a.dequeue()
a.display()
'''
