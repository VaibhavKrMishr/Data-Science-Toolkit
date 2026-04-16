import numpy as np

# a= np.array([85,92,78,88,90])
##Take user Input for multiple students 

rows = int(input("Enter the number of students: "))
cols = int(input("Enter the number of subjects/grades: "))

print(f"Enter all {rows * cols} grades/scores space-separated in a single line:")
    
vals = list(map(int, input().split()))
student_data = np.array(vals).reshape(rows, cols)

avg=student_data.mean()
for i in range(rows):
    print("Average Grade: ",avg)
    Grade =''
    if(int(avg) in range(90,100)):
        Grade ="A"
    if(int(avg) in range(80,90)):
        Grade ="B"
    if(int(avg)in range(70,80)):
        Grade ="C"
    if(int(avg) in range(60,70)):
        Grade ="D"
    if(int(avg) in range(0,60)):
        Grade ="F"
    print("Letter Grade: ",Grade)