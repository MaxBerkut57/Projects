# Мой вариант
def twoSum(nums: list, target: int):
    seen = set()
    for i, num in enumerate(nums):
        b = target - num
        seen.add(b)
        if num in seen:
            idx = nums.index(b)
            if i != idx:
                return [i, idx]


# Вариант claude
def two_sum(nums: list, target: int):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").strip().split()))
    target = int(input("Enter target: "))
    print(twoSum(nums, target))
    print(two_sum(nums, target))
