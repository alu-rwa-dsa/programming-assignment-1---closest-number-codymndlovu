#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    sorted_arr = sorted(arr)
    min_diff = sorted_arr[1] - sorted_arr[0]
    min_diff_pairs = []
    
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i+1] - sorted_arr[i] == min_diff:
            min_diff_pairs += [sorted_arr[i], sorted_arr[i+1]]
        elif sorted_arr[i+1] - sorted_arr[i] < min_diff:
            min_diff = sorted_arr[i+1] - sorted_arr[i]
            min_diff_pairs = [sorted_arr[i], sorted_arr[i+1]]
            
    return min_diff_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
