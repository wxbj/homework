import copy


# 并两个已排序好的列表，产生一个新的已排序好的列表
def merge(initial_list, left, mid, right):
    # 用来记录第一个列表的启示序号[left,low)
    i = left
    # j用来记录第二个列表的启示序号[low,right)
    j = mid
    # 临时存储原始列表,用于后面的合并
    temp_list = copy.deepcopy(initial_list)

    # 通过一次循环完成合并
    for k in range(left, right):
        # 第一个有序子数组已经遍历完
        if i >= mid:
            initial_list[k] = temp_list[j]
            j = j + 1
        # 第二个有序子数组已经遍历完
        elif j >= right:
            initial_list[k] = temp_list[i]
            i = i + 1
        # 第一个有序子数组的元素较小时
        elif temp_list[i] < temp_list[j]:
            initial_list[k] = temp_list[i]
            i = i + 1
        # 第二个有序子数组的元素较小时
        else:
            initial_list[k] = temp_list[j]
            j = j + 1


# 二分归并排序的非递归实现
def binary_merge_sort():
    initial_list = [5, 4, 3, 0, 1, 2, 7, 6, 11, 9, 20, 15, 6]
    i = 1
    # 2分法,子数组长度是1、2、4、8这样的
    while i < len(initial_list):
        left = 0
        # 这里是两两合并相邻的两个有序子数组,如果最后就剩一个就无需合并了
        while left < len(initial_list):
            mid = left + i
            right = min(left + 2 * i, len(initial_list))
            if mid < right:
                merge(initial_list, left, mid, right)
            left += 2 * i
        i *= 2
    print(initial_list)


if __name__ == "__main__":
    binary_merge_sort()
