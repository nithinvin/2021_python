def containsDuplicate(nums) -> bool:
    unique_list = []
    for num in nums:
        if num in unique_list:
            return True
        else:
            unique_list.append(num)
    return False


list1 = [1,1,1,3,3,4,3,2,4,2]
print ("Contains duplicate returns", containsDuplicate(list1))