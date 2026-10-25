name = input("enter student name:")
n = int(input("enter number of students"))
t=0
for i in range(1,n+1):
    mark = float(input(f"enter mark for studen {i}:"))
    t+= mark
    p = t/n
    if p >= 90:
        grade = "A+"
        per = "Outstanding"
    elif p >= 80:
            grade = "A"
            per = "Excellent"
    elif p >= 70:
            grade = "B"
            per = "very good"
    elif p >= 60:
            grade = "C"
            per = "Good"
    elif p >= 50:
            grade = "D"
            per = "Average"
    else :
           grade="F"
           per = "Needs Improment"
print("\n ---Academic Performance ---")
print("student name : ",name)
print("Total Marks :",t)
print("percentage :",round(per,2),"%")
print("Grade      :",grade)
print("performance:",per)






