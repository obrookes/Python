'''
Google: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

from itertools import combinations

def satisfying_k(real_numbers, k, n):
    combos = combinations(real_numbers, n)
    for comb in list(combos):
        if(sum(comb) == k):
            return True
    return False

r = [10, 15, 3, 7]
k = 17
n = 2

if(satisfying_k(r, k, n)):
    print("True")
