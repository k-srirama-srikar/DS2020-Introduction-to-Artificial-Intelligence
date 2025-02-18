def upheap(arr,i=-1):
    if i==0:
        # the base case which means that the inserted value has been placed at the top
        
        return
    if i == -1:
        # base parameter which implies that its the last element
        i = len(arr)-1
        p = int((i-1)/2)
        # p is the parent's index
        if arr[p] > arr[i]:
            # the heap property is satisfied
            return
        else:
            arr[p], arr[i] = arr[i], arr[p]
            # we swap the values and call the upheap function again
            
            return upheap(arr=arr, i=p)
    else:
        # general case
        p = int((i-1)/2)
        if arr[p] > arr[i]:
            # the heap property is satisfied
            return
        else:
            arr[p], arr[i] = arr[i], arr[p]
            
            return upheap(arr=arr, i=p)
        
def heapify(arr):
    temp = []
    # temporary heap
    for a in arr:
        temp.append(a)
        upheap(arr=temp)
    for i in range(0,len(temp)):
        # in order to make sure the sorting is done in-place
        arr[i] = temp[i]
    i
        

def sort_op(arr, i=-1):
    if i==-1:
        # the case where the element is the last element
        i = len(arr)-1
    if i==0:
        
        return
    arr[0], arr[i] = arr[i], arr[0]
    
    downheap(arr=arr, n=i)
    i -= 1
    sort_op(arr=arr, i=i)


def downheap(arr, n, i=0):
    if n==1:
        
        return
    c1 = 2*i+1
    c2 = 2*i+2 
    if c1< n and c2<n:
        # n makes sure that the size of the heap is reduced with every swap
        if arr[c1] < arr[c2]:
            c1, c2 = c2, c1
            # just to make sure that the heap property is maintained
    # checking if any of the two childeren violate the heap property
    if c1<n:
        if arr[i] < arr[c1]:
            arr[i], arr[c1] = arr[c1], arr[i]
            
            return downheap(arr=arr, n=n, i=c1)
    if c2<n:
        if arr[i] < arr[c2]:
            arr[i], arr[c2] = arr[c2], arr[i]
            
            return downheap(arr=arr, n=n, i=c2)
    return
    

def HeapSort(arr):
    heapify(arr=arr)
    # Step 1 - Heapify
    sort_op(arr)
    # Step 2 - Sort the Heap
    print("Array after HeapSort:",arr)
    return arr


arr = [34,56,78,21,10,4,0,6]
HeapSort(arr)

# the following line can be uncommented to check if it was inplace or not
print("T make sure that it is in-place:",arr)


