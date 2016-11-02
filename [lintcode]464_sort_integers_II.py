#!/usr/bin/env python
# coding=utf-8
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        if not A:
            return A
        stack=[]
        stack.append((0, len(A) - 1))
        while stack:
            left, right = stack.pop()
            if left >= right:
                continue
            i, j = left, right
            pivot = A[(i + j) / 2]
            while i <= j:
                while i <= j and A[i] < pivot:
                    i += 1
                while i <= j and A[j] > pivot:
                    j -= 1
                if i<= j:
                    A[i], A[j] = A[j], A[i]
                    i, j = i + 1, j - 1
            stack.append((left, j))
            stack.append((i, right))
