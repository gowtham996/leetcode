gas=[5,1,2,3,4]
cost = [4,4,1,5,1]
if sum(gas) < sum(cost): print(-1)
startindex=0
currentgas=0
for i in range(len(gas)):
    currentgas+=gas[i]-cost[i]
    if currentgas < 0:
        currentgas=0
        startindex=i+1
print(startindex)
