g=g = [1,4]
s = [1,2,3]
g.sort()
s.sort()
output=0

j=0
for i in range(len(s)):
    if g[j]<=s[i]:
        j+=1
        output=output+1
        if j==len(g):
            break
print(output)