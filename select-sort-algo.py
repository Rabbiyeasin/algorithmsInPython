def sort(arrays):
    length = len(arrays)
    
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arrays[j] < arrays[min_index]:
                min_index = j
        
        # Swap if the minimum is not the current position
        if min_index != i:
            arrays[i], arrays[min_index] = arrays[min_index], arrays[i]

def main():
    scores = [60, 80, 95, 50, 70]
    sort(scores)
    for score in scores:
        print(score, end=", ")

if __name__ == "__main__":
    main()
