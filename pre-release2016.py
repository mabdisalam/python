
# Arrays or in python we call it a list that will store student names 
studentNames=[]
studentMarkstest1=[]
studentMarkstest2=[]
studentMarkstest3=[]
studentTotalScore=[]
sum=0
TopName=""
highestScore=0
for count in range(3):
    print("Enter student's name:")
    name =input()
    studentNames.append(name)
    print("Student's name:", studentNames)
    
    test1=21
    while test1 > 20:
         print("Test 1 is out of 20 marks")
         print("Enter first mark")
         test1=int(input())
        
        
    studentMarkstest1.append(test1)
    print(studentMarkstest1)
    
    test2=26
    while test2 > 25:
         print("Test 2 is out of 25 marks")
         print("Enter second mark")
         test2=int(input())
    studentMarkstest2.append(test2)
    print(studentMarkstest2)
    
    test3=36
    while test3 > 35:
        print("Test 3 is out of 35 marks")
        print("Enter third mark")
        test3=int(input())
    studentMarkstest3.append(test3)
    print(studentMarkstest3)

#Task 2
#  the total score for each student and store in the array. Calculate the average total score for the whole class. */

    print("Total marks for", name,":")
    total=test1+test2+test3
    print(total)
    studentTotalScore.append(total)

    print("studentTotalScore", studentTotalScore)

    sum=sum+total
    print("sum's of students' total marks", sum)
    #Task 3
    #Student with the highest score

    if total > highestScore:
        highestScore = total
        TopName = studentNames[count]
class_average=sum/3
print("Class average: ", class_average)

#Task 3
    #Student with the highest score

    
    
print(TopName, "got the higest score: ", highestScore)
