#program to accept name, rollno,marks and find total and percentage
name=input("enter name of student ")
rollno=input("enter rollno ")
science=int(input("enter marks in sub science "))
maths=int(input("enter marks in sub maths "))
geo=int(input("enter marks in sub geo "))

total=science+maths+geo
perc=total/3


print("Roll no is ",rollno)
print("Name is ",rollno )
print("Total is ",total)
print("Perc is ",perc)
