from re import T


def containsDuplicate(nums) -> bool:
    import bisect
    from bisect import bisect_left
    unique_list = []
    for num in nums:
        llen = len(unique_list)
        index = bisect_left(unique_list, num)
        #print("Unique_list", unique_list, "Index:", index, "llen", llen)
        if llen != 0 and index < llen and unique_list[index] == num:
            return True
        else:
            bisect.insort(unique_list, num)
    return False


list1 = [1, 2, 3, 4]
print ("Contains duplicate returns", containsDuplicate(list1))