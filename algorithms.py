#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 07:27:20 2018

@author: sidharthsuman
"""
# searching algorithms

def bruteforce_search(n_list,data):
    index = -1
    for i in range(0,len(n_list)):
        if(n_list[i]==data):
            print('index of data ',i)
            index = i
            return(index)
    print('Data not found')
    return
    
def binary_search(n_list,data):
    start = 0
    end = len(n_list)-1
    found = False
    while(start<=end and not found):
        mid = (start+end)//2
        if(n_list[mid]==data):
            found = True
            return(mid)
        elif(n_list[mid]<data):
            start = mid+1
        else:
            end = mid+1
    return(-1)

# sorting algorithms

def swap(n_list,first_index,second_index):
    temp = n_list[first_index]
    n_list[first_index] = n_list[second_index]
    n_list[second_index] = temp
    return(n_list)

def find_next_min(n_list,i):
    min_num = n_list[i]
    min_index = i
    for j in range(i,len(n_list)):
        if(n_list[j] < min_num):
            min_num = n_list[j]
            min_index = j
    return(min_index)
            
def selection_sort(n_list):
    for i in range(0,len(n_list)):
        min_index = find_next_min(n_list,i)
        swap(n_list,i,min_index)
    return(n_list)

def bubble_sort(n_list):
    for i in range(0,len(n_list)):
        done = False
        for j in range(1,len(n_list)-i):
            if(n_list[j] < n_list[j-1]):
                swap(n_list,j,j-1)
                done = True
        if(done == False):
            break
    return(n_list)
    
nlist=[6,5,3,2,4,1,7,9,10,8]
print(bubble_sort(nlist))


