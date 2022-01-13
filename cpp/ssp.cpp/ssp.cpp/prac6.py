def InsertSort(arr, n):
    i = 1
    for i in range(n):
        temp = arr[i]
        j = i-1
        while((j >= 0) & (arr[j] > temp)):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp

    print(arr)
    print("Top Five Scores are...")
    for i in range(len(arr)-1, 1, -1):
        print(arr[i])


def ShellSort(arr, n):
    d = n//2
    while d > 0:
        for i in range(d, n):
            temp = arr[i]
            j = i
            while(j >= d and arr[j-d] > temp):
                arr[j] = arr[j-d]
                j -= d

            arr[j] = temp
        d = d//2

    print(arr)
    print("Top Five Scores are...")
    for i in range(len(arr)-1, 1, -1):
        print(arr[i])


# Driver Code
print("\nHow many students are there?")
n = int(input())
array = []
i = 0
for i in range(n):
    print("\n Enter percentage marks")
    item = float(input())
    array.append(item)

print("You have entered following scores...\n")
print(array)
while(True):
    print("Main Menu")
    print("\n 1. Insertion Sort")
    print("\n 2. Shell Sort")
    print("\n 3. Exit")
    print("\n Enter your Choice: ")
    choice = int(input())
    if(choice == 1):
        print("\n The sorted Scores are...")
        InsertSort(array, n)
    elif(choice == 2):
        print("\n The sorted Scores are...")
        ShellSort(array, n)
    else:
        print("Exitting")
        break
