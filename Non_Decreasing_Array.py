def Non_Decreasing_Array(arr,n):
  v=0
  for i in range(n-1):
    if arr[i]>arr[i+1]:
      v+=1
      if v>1:
        return False
    if i>0 and arr[i-1] > arr[i+1]:
      arr[i+1]=arr[i]
    else:
      arr[i]=arr[i+1]
  return True
