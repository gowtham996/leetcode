def findSecondLargest(sq):
    newarr=list(set(sq))

    newarr.sort()

    if len(newarr)<2:
        return -1
    else:
        return newarr[-2]
