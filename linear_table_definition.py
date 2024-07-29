#linear Table : Sequence of elements, is a one dimensional array 

# Define a one dimensional array of student scores 
#where : 
# 0  | 1  | 2  | 3  | 4  | 5  | : array loaction 
# 90 | 70 | 50 | 80 | 60 | 85 | : array value
#array length = 6 

import sys
def main():
    scores = [90,70,50,80,60,85]
    length = len(scores)

    for i in range(0,length):
        print(scores[i],",",end="")

if __name__ == "__main__": 
    main()
