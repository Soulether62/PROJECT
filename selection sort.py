def selectionsort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if(arr[min_index]>arr[j]):
                min_index=j
        temp=arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=temp
    print(arr)
    return arr
arr=[10,50,80,20,30,60,65,63,69,36,38,100,105,102,10,3]
selectionsort(arr)