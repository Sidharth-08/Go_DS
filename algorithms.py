#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 07:27:20 2018
Updated on Sat May  5 11:31:00 2018

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

def merge(left_list,right_list):
    merged_list = []
    i=0
    j=0
    while(i<len(left_list) and j<len(right_list)):
        if(left_list[i]<=right_list[j]):
            merged_list.append(left_list[i])
            i+=1
        elif(left_list[i]>right_list[j]):
            merged_list.append(right_list[j])
            j+=1
    while(i<len(left_list)):
        merged_list.append(left_list[i])
        i+=1
    while(j<len(right_list)):
        merged_list.append(right_list[j])
        j+=1
    return(merged_list)

def merge_sort(n_list):
    i=0
    j=len(n_list)-1
    if(i==j):
        return(n_list)
    else:
        mid = (i+j)//2
        sorted_left_list = merge_sort(n_list[i:mid+1])
        sorted_right_list = merge_sort(n_list[mid+1:j+1])
        sorted_list = merge(sorted_left_list,sorted_right_list)
        return(sorted_list)

def partition(n_list,low,high):
    pivot = n_list[low]
    left = low+1
    right = high
    done = False
    while not done:
        while(pivot >= n_list[left] and left <= right):
            left+=1
        while(pivot <= n_list[right] and right >= left):
            right-=1
        if(left > right):
            done = True
        else:
            swap(n_list,left,right)

    swap(n_list,low,right)
    return(right)


def quick_sort_helper(n_list,low,high):
    if(low < high):
        partit = partition(n_list,low,high)
        quick_sort_helper(n_list,low,partit-1)
        quick_sort_helper(n_list,partit+1,high)
    return(n_list)

def quick_sort(n_list):
    sorted_list = quick_sort_helper(n_list,0,len(n_list)-1)
    return(sorted_list)

# driver code
n_list=[6,5,3,2,4,1,7,9,10,8]
print(quick_sort(n_list))
