nums = [5]
target = 5


# У этой функции сложность O(log n) - для списка с 1 000 000 элементов нужно всеголишь 20 шагов, так как данныц алгоритм делит на каждой итерации список пополам
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(search(nums, target))
