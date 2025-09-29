m_1 = int(input("enter a number: "))
m_1 = int(input("enter a number: "))
m_2 = int(input("enter a number: "))
m_3 = int(input("enter a number: "))
m_4 = int(input("enter a number: "))
m_5 = int(input("enter a number: "))

total = m_1 + m_2 + m_3 + m_4 + m_5
avg = total / 500 * 100
print("total marks: ", total)

print("percentage marks: ", avg)
if avg >= 90:
    print("grade A")
elif avg >= 75:
    print("grade B")
elif avg == 50:
    print("grade C")
elif avg >= 35:
    print("grade D")
else:
    print("sorry you are fail")



marks = [int(input("enter marks: ")) for i in range(5)]  # this another method

total = sum(marks)
avg = total / 500 * 100
grade = "A" if avg >= 90 else "B" if avg >= 75 else "C" if avg >= 50 else "D" if avg >= 35 else "F"

print("Total Marks:", total)
print("Percentage:", avg)
print("Grade:", grade)