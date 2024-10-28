def insert_and_sort(arr, new_score):
    # Create a new array with an extra space for the new score
    temp_array = arr + [0]  # Append a placeholder for the new score
    i = len(arr) - 1
    
    # Find the correct position for the new score
    while i >= 0 and arr[i] > new_score:
        temp_array[i + 1] = arr[i]
        i -= 1
    
    # Insert the new score
    temp_array[i + 1] = new_score
    
    return temp_array

def main():
    scores = [90, 70, 50, 80, 85]
    new_score = 75
    sorted_scores = insert_and_sort(scores, new_score)
    
    for score in sorted_scores:
        print(score, end=", ")

if __name__ == "__main__":
    main()
