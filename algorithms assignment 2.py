import winsound  # Import the winsound module for sound effects

def merge_sort(arr):
    # Recursive function to implement merge sort
    if len(arr) > 1:
        # Find the middle index(pivot) of the array
        mid = len(arr) // 2
        left_half = arr[:mid]  # Divide the array into left half
        right_half = arr[mid:]  # Divide the array into right half
        
        # Recursively sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Initialize pointers for left, right, and merged array
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                # Play a sound effect for the swap
                winsound.Beep(500, 400)  # Beep with frequency 500Hz for 200 milliseconds
            k += 1

        # Copy the remaining elements of left half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of right half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Main function to demonstrate merge sort
    array = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    print("Given Array:", array)
    merge_sort(array)
    print("Sorted(by mergesort) Array:", array)

if __name__ == "__main__":
    main()
