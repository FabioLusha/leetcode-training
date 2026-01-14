def solution(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()

    print(nums)
    if len(nums) % 2 != 0:
        # Not +1 because of 0-based indexing
        return nums[len(nums) // 2]
    else:
        print("Second clause")
        middle_point = len(nums) // 2
        return (1 / 2) * (nums[middle_point - 1] + nums[middle_point])
