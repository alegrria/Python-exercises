#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:07:22 2017

@author: annakizilova
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1, bag2 = [], []
        #creating two empty lists for storing items
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
                #The shift operator >> shifts all digits to the right X times, 
                #where X is the number on the right of the >> operator. 
                #For example, 8 (which is equal to 1000) >> 1, will shift the 
                #4 digits 1 step to the right to be (0100) which is equal to 4.
                #Even numbers in binary always have 0 as the first digit on the
                #right whereas odd numbers have 1 as the first number on the right. 
                #So, 8 (1000) has 0 on the right .. when we shift it right by 
                #1 .. 4(0100) has 0 on the right, 2(0010) has 0 on the right ..
                #1(0001) has 1 on the right. So, if we check if the number is 
                #odd or not, we can know if there is 1 on the right or not.
                #Using this idea, the code tries to shift each different combination 
                #by numbers from 0 to N, each time it checks if it's odd or not by 
                #checking if there's a remainder of 1 (if (i >> j) % 2 == 1) .. 
                #if so, then the number of times we shifted the current combination 
                #(j in this case) is the original position of the 1 in the 
                #combination .. which we can use as an index for the corresponding 
                #item we want to take.
                #So if the current combination is 1000 (8) and by shifting it 3 
                #times to the right we have 0001 which is odd, we know that 1 in 
                #1000 is the 3rd bit (starting from 0 from the right to the left). 
                #if the list of items are [rice, meat, egg, juice] then items[3] is juice.
                #So, for each different combination, we use the binary 
                #representation of that combination and use the previous 
                #method to search for the 1's in the number and add the 
                #corresponding items to the list of the items to be taken.
            if (i // 3**j) % 3 == 2:
                bag2.append(items[j])
                #
        yield (bag1, bag2)


def yieldAllCombos4(items):
    """
      Generates all combinations of N items into three bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2, bag3), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 4**N possible combinations
    for i in range(4**N):
        bag1, bag2, bag3 = [], [], []
        #creating three empty lists for storing items
        for j in range(N):
            # test bit jth of integer i
            if (i // 4**j) % 4 == 1:
                bag1.append(items[j])
            if (i // 4**j) % 4 == 2:
                bag2.append(items[j])
            if (i // 4**j) % 4 == 3:
                bag3.append(items[j])
        yield (bag1, bag2, bag3)