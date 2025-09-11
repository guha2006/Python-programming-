name=input("enter your name:")
rollno=int(input("Enter your roll.no:"))
m1=int(input("Enter your first mark:"))
m2=int(input("Enter your second mark:"))
m3=int(input("Enter your third mark:"))
m4=int(input("Enter your fourth mark:"))
m5=int(input("Enter your fifth mark:"))
total=m1+m2+m3+m4+m5
print("total:",total)
avg=total/5
print("avg:",avg)
if m1<40:
    print("Fail")
elif m2<40:
    print("Fail")
elif m3<40:
    print("Fail")
elif m4<40:
    print("Fail")
elif m5<40:
    print("Fail")
else:
    print("pass")
    print("grade of student")
if avg>=90 and avg<=100:
    print("A grade")
elif avg>=80 and avg<=90:
    print("B grade")
elif avg>=70 and avg<80:
    print("C grade")
elif avg>=60 and avg<=70:
    print("D grade")
else:
    print("E grade")
    
