def Binsearch(arr, KEY):
    low = 0
    high = len(arr)-1
    m = 0
    while(low <= high):
        m = (low+high)//2  # mid of the array is obtained
        if(KEY < arr[m]):
            high = m-1  # search the left sub list
        elif(KEY > arr[m]):
            low = m+1  # search the right sub list
        else:
            return m

    return -1  # if element is not present in the list


def FibSearch(arr, key, n):
    # Initialize Fibonacci numbers
    b = 0
    a = 1
    f = b + a

    # f is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while (f < n):
        b = a
        a = f
        f = b + a
      # Marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected.
    # we compare arr[i] with key.
    while (f > 1):

        # Check if b is a valid location
        i = min(offset+b, n-1)

        # If key is greater than the value at
        # index b, cut the subarray array
        # from offset to i
        if (arr[i] < key):
            f = a
            a = b
            b = f - a
            offset = i

        # If key is lesser than the value at
        # index b, cut the subarray
        # after i+1
        elif (arr[i] > key):
            f = b
            a = a - b
            b = f - a

        # element found. return index
        else:
            return i

    # comparing the last element with key
    if(a and arr[offset+1] == key):
        return offset+1

    # element not found. return -1
    return -1


# Driver Code
print("\nHow many Students are there?")
n = int(input())
array = []
i = 0
for i in range(n):
    print("\n Enter roll number: ")
    item = int(input())
    array.append(item)

print("The Roll Numbers of Students are ...\n")
print(array)


while(True):
    print("Main Menu")
    print("\n 1. Binary Search")
    print("\n 2. Fibonacci Search")
    print("\n 3. Exit")
    print("\n Enter your choice: ")
    choice = int(input())
    if(choice == 1):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = Binsearch(array, key)
        if(location != -1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    elif(choice == 2):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = FibSearch(array, key, n)
        if(location != -1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    else:
        print("Exitting")
        break
