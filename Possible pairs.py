"""
Given an array of numbers, print all possible pairs of numbers.
And remove the duplicates, that is, (1,2) is the same as (2,1).
Example:
numbers = [1,2,3,4]
pairs are (1,1),(1,2),(1,3),(1,4),(2,1)(2,2)... but you have to remove the duplicate
"""

numbers = [1,2,3,4]

for i in range(len(numbers)-1):
  for j in range(i+1, len(numbers)):
    print (numbers[i], "-->", numbers[j])
