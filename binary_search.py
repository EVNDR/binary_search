def binarysearch(thelist,item):
    if len(thelist) == 0:
        return False
    else:
        midpoint = len(thelist)//2
        if (thelist [midpoint] == item):
            return True
        else:
            if item < thelist[midpoint]== item:
                return binarysearch(thelist[:midpoint],item)
            else:
                return binarysearch(thelist[midpoint+1:],item)            