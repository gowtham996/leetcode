a = [[1, 2], [2, 3], [3, 4]]
count=1
sorted_a = sorted(a, key=lambda x: x[1])
prev=a[0][1]
i=1
while i<len(a):
    if a[i][0]>prev:
        count+=1
        prev=a[i][0]
    i+=1
print(count)