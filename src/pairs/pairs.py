from data_sets import large_list, case_one_list, case_two_list, case_three_list


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(large_list, 19999))
    print(s.twoSum(case_one_list, 9))
    print(s.twoSum(case_two_list, 6))
    print(s.twoSum(case_three_list, 6))
