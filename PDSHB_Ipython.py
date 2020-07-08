# Date Last Modified: 02/07/2020
# Author: Pedro H. Puntel
# Email: pedro.puntel@gmail.com
# Topic: Python Data Science Handbook - Reference Script
# Ecoding: UTF-8

###########################################
# Chapter I: Ipython - Beyond Normal Python
###########################################

# Accessing documentation and source code
import numpy as np
?np.array
??np.array

# Tip: Use tab-completion for faster typing
# Usage: np.a<tab>

# Wildcard matching
# Useful when we want to search for a function that we already know what it may look like
*Warning?

# Line Magics (%) - They act on a single line of code
%timeit -r 100 L = [i**2 for i in range(1000)]

# Cell Magics (%%) - They act on a entire chunk of code
%%timeit -r 100
L = []
for i in range(1000):
    L.append(i**2)

# In and Out are not just pretty objects, they hold data about previous inputs and outputs
print(In[5]) # In is a list whose indexes are the previously provided inputs
print(type(Out)) # Out is an dictionary whose keys are the provided inputs and values are the actual outputs

# Suppresing output - (;)
import math
math.sin(0); # Useful in matplotlib when we don't want to see '<matplotlib.pyplot.axes at 0x....>'

# Timing Code Snippets - Which operation is faster ?
%timeit -r 10 sum(range(1000))
%%timeit -r 10
total=0
for i in range(1000):
    for j in range(1000):
        total += i * (-1) ** j

# Sometimes repeating an operation is not the best option since we might be mislead by repating it
import random
L = [random.random() for i in range(100000)]
print("Sorting an unsorted list:")
%time L.sort()
print("Sorting an already sorted list:")
%time L.sort()

# Profiling full scripts - Identify bottlenecks in our code
def sum_of_lists(N):
    total=0
    for i in range(5):
        L = [j^ (j>>i) for j in range(N)]
        total += sum(L)
    return total

%prun sum_of_lists(1000000)

# Line-By-Line Profiling - Even more clue on the bottlenecks in our code
import line_profiler
%load_ext line_profiler
%lprun -f sum_of_lists sum_of_lists(5000)

# Profiling Memory Usage - Sometimes memory is more of a concern then speed
import memory_profiler
%load_ext memory_profiler
%memit sum_of_lists(1000000)

