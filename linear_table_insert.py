def insert(array, score, insertIndex):
    length = len(array)
    tempArray = [0 for _ in range(length + 1)]  # Corrected typo here
    
    for i in range(length):
        if i < insertIndex:
            tempArray[i] = array[i]  # Copy elements before the insert index
        else:
            tempArray[i + 1] = array[i]  # Shift elements to the right
    
    tempArray[insertIndex] = score  # Insert the new score at the specified index
    return tempArray

def main():
    score = [90, 70, 50, 80, 60, 85]
    score = insert(score, 75, 2)  # Insert 75 into index position 2 
    length = len(score)
    
    for i in range(length):
        print(score[i], end=", ")
    print()  # For better formatting, to move to the next line

if __name__ == "__main__":
    main()
