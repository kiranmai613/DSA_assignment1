def count_pairs_with_sum(arr, sum):
    freq = {}
    count = 0
    
    for num in arr:
        target = sum - num
        
        if target in freq:
            count += freq[target]
        
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return count
arr = [1,5,7,-1,5]
sum=6
print(count_pairs_with_sum(arr, sum))