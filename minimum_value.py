#Algorithmic ideas
#Initial value minIndex=0, j=1 Compare arrays[minIndex] with arrays[j] if arrays[minIndex] > arrays[j] then minIndex=j, j++ else j++. continue until the last number, arrays[minIndex] is the Min Value

import sys

def min(arrays):
    minIndex = 0;
    length = len(arrays)-1
    for j in range(0,length):
        if(arrays[minIndex]>arrays[j]):
            minIndex =j
        return arrays[minIndex]

def main():
    scores =[60,80,95,50,70]
    minValue = min(scores)
    print("Min Value =",minValue)

if __name__=="__main__":
    main()