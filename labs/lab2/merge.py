def merge_sort(data):
    # Base case: if the list has only one element, it's already sorted
    if len(data) <= 1:
        return data
    
    # Divide the list into two halves
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    
    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    while left and right:
        # Compare the integer part of the tuple (index 1)
        if left[0][1] <= right[0][1]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    
    # If there are remaining elements in either left or right, add them
    sorted_list.extend(left)
    sorted_list.extend(right)
    
    return sorted_list

# Example usage:
data = [
    [(1, 5), 10],
    [(1, 3), 5],
    [(1, 10), 5]
]

sorted_data = merge_sort(data)
print(sorted_data)
