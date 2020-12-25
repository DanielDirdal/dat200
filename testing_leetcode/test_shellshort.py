def shellSort(alist):
    sublistcount = 5
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = (sublistcount // 2)
      if sublistcount == 2:
          sublistcount = 3


def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [3, 7, 5, 8, 10, 15, 12, 14, 18, 23]
shellSort(alist)
print(alist)