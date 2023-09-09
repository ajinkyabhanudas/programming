"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""


class Solution:
    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        map_dict = {}
        for i, num in enumerate(nums):
            if num not in map_dict:
                map_dict[target-num] = i
            else:
                return [map_dict[num], i]


def main():

    input_list = [int(x) for x in input("Key-in the space separated integer list elements: ").split()]
    target = int(input("Key-in the target sum: "))

    result_list = Solution.two_sum(input_list, target)

    if result_list and input_list[result_list[0]]+input_list[result_list[1]] == target:
        print(f"\nThe solver works correctly:\ntarget: {target}\nelement indices: {result_list}\n")
    else:
        print(f"result_list: {result_list}\ntarget: {target}\nsolver result: {input_list[result_list[0]]+input_list[result_list[1]]}")

if __name__ == "__main__":
    main()