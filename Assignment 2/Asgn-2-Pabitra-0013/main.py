def delete_all_duplicates_unordered(nums):
    return list(set(nums))

test_list = [5, 1, 2, 1, 2, 3, 5, 4, 1,1,6]
print(delete_all_duplicates_unordered(test_list))