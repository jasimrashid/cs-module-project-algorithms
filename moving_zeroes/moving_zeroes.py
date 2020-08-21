'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    shift = 0
    arr2 = [0]*len(arr)
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr2[j] = arr[i]
            j += 1
    return arr2



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0,0,0,0,3,2,1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")