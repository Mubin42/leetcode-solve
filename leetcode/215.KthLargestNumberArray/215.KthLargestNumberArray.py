"""
215. Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1200582321/
Status: Solved
"""


def findKthLargest(nums, k):
    sorted_nums = sorted(nums)
    res = sorted_nums[len(sorted_nums) - k]
    print(sorted_nums)

    return res


if __name__ == "__main__":
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    result = findKthLargest(nums=arr, k=4)
    print(result)

