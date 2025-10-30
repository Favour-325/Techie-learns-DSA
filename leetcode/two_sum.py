class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for num in range(len(nums)):
            hash_table = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hash_table:
                    return [i, hash_table[complement]]
                
                hash_table[nums[i]] = i


def main():
    solve = Solution()

    nums = list(map(int, input("Numbers: ").split()))
    target = int(input("Target: "))
    result = solve.two_sum(nums, target)

    print(result)


if __name__ == "__main__":
    main()