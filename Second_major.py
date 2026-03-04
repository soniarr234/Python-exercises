"""
Dado un listado de números, encuentra el SEGUNDO más grande
"""

nums = [3, 6, 2, 1, 7]

for i in range (len (nums)):
    for j in range (i+1, len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

second_major = nums[1]
print(second_major)
