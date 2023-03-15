def find_duplicates(arr):
    freq = {}
    duplicates = []
    
    for num in arr:
        if num in freq:
            duplicates.append(num)
        else:
            freq[num] = 1
            
    return duplicates
arr = [1, 2, 3, 1, 4, 2, 5]
print(find_duplicates(arr))  # Output: [1, 2]
