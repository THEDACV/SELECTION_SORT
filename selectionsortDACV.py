def selection_sort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]< arr[min_idx]:
                min_idx=j
                arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

#Example usage
unsorted_list=[64,25,22,11]
sorted_list=selection_sort(unsorted_list)
print("sorted array is :" , sorted_list)
