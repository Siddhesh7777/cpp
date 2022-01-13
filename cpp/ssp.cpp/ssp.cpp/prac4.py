def Linsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def Sentsearch(arr, x):
    l = len(arr)
    arr.append(x)
    i = 0
    while(arr[i] != x):
        i = i+1
    if(i != l):
        return i
    else:
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
    print("\n 1. Linear Search")
    print("\n 2. Sentinel Search")
    print("\n 3. Exit")
    print("\n Enter your choice: ")
    choice = int(input())
    if(choice == 1):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = Linsearch(array, key)
        if(location != -1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    elif(choice == 2):
        print("\n Enter the roll number to search if student has attended the training program or not? ")
        key = int(input())
        location = Sentsearch(array, key)
        if(location != -1):
            print("Yes, the student attended the training program!!!")
        else:
            print("No, the student has not attended the training program!!!")
    else:
        print("Exitting")
        break

