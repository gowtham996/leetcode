def maxswap(nums):
    num_list = [int(digit) for digit in str(num)]
    lastindex={val:i for i, val in enumerate(num)}

    for i in range(len(num)):
        for d in range(9,num[i],-1):
            if d  in lastindex and lastindex[d]>1:
                num[1],num[lastindex[d]]=num[lastindex[d]],num[i]
                return (int("".join(map(str.num))))
            
    return num
num=2736
print(maxswap(num))