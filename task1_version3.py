sum = 0
studentsName=[]
studentsMarkstest1=[]
studentsMarkstest2=[]
studentsMarkstest3=[]
studentsTotalScore=[]
bestName=""
highestScore=0
for count in range(3):
    print("Enter student's name:")
    name =input()
    studentsName.append(name)
    print("Student's name:", studentsName)
    print("Enter first mark")

    test1=int(input())
    studentsMarkstest1.append(test1)
    print(studentsMarkstest1)
    print("Enter second mark")
    test2=int(input())
    studentsMarkstest2.append(test2)
    print(studentsMarkstest2)
    print("Enter third mark")
    test3=int(input())
    studentsMarkstest3.append(test3)
    print(studentsMarkstest3)
    print("Total marks for", name,":")
    total=test1+test2+test3
    print(total)
    studentsTotalScore.append(total)
    
    print("studentsTotalScore", studentsTotalScore)
    if total > highestScore:
        highestScore = total
        bestName = studentsName[count]
    sum=sum+total
    print("sum's of students' total marks", sum)
class_average=sum/3
print("Class average: ", class_average)
print(bestName, "got the higest score: ", highestScore)
