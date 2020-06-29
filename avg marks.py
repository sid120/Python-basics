name=input("enter name of student ")
rollno=input("enter rollno ")
science=int(input("enter marks in sub science "))
maths=int(input("enter marks in sub maths "))
geo=int(input("enter marks in sub geo "))
eng=int(input("enter marks in sub eng "))
histroy=int(input("enter marks in sub histroy "))

total=science+maths+geo+eng+histroy
avg=total/5


print("Roll no is ",rollno)
print("Name is ",name)
print("Total is ",total)
print("Avg is ",avg)
