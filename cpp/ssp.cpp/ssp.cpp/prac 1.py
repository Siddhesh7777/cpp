marks= []
def getdata():
    print("-----FDS Exam Details-----")
    print("Enter the no. of students: ")
    #global marks
    N = int(input())
    for i in range(N):
        print("Enter the marks of students (marks out of 30, enter -1 if absent): ")
        M= float(input())
        marks.append(M)
    print("Marks of Students: ", marks)

def average():
    avg=0
    count=0
    for i in range(len(marks)):
        if marks[i] != -1:
            avg= avg + marks[i]
            count = count +1
    print("Average Marks= ", avg/count)

def high_score():
    high= marks[0]
    for i in range(len(marks)):
        if marks[i] != -1:
            if high < marks[i]:
                high= marks[i]
    print("Highest Score= ", high)

def low_score():
    low= marks[0]
    for j in range(len(marks)):
        if marks[j] != -1:
            if low > marks[j]:
                low= marks[j]
    print("Lowest Score= ", low)

def absent_count():
    count_absent=0
    for i in range(len(marks)):
        if marks[i] == -1:
            count_absent= count_absent +1
    print("No. of students absent= ", count_absent)

def high_freq():
    freq= []
    for i in range(len(marks)):
        if marks[i] != -1:
            freq.append(marks.count(marks[i]))
    print(freq)
    k= max(freq)
    print("Highest frequency= ", k, "of marks= ", max(set(marks)) )

getdata()
average()
high_score()
low_score()
absent_count()