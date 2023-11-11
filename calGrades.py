def calcaverage (grades, n):
    total = 0
    for each in grades:
        total += each
        
    average = total / n
    return average        
        
def determinegrade (i):
    o = []
    for each in i:
        if each >= 90:
           o.append("Letter A")
        elif each >= 80:
          o.append("Letter B")
        elif each >= 70:
            o.append("Letter C")
        elif each >= 60:
            o.append("Letter D")
        else:
            o.append("Letter F")
    return o

        

test = 1
grades = []
n = int(input("enter the number of test grades "))
for x in range (n):
        x = int(input("test " + str(test) + ": " ))
        grades.append(x)
        test = test + 1

averageScore = calcaverage(grades, n)
print("The average score is " + str(averageScore))
    
letterGrade = determinegrade(grades)
print(letterGrade)