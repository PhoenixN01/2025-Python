score = [95, 67, 83, 38, 59]
grade = []

for n in score:
    if n >= 80:
        grade.append("A")
    elif n >= 60:
        grade.append("B")
    elif n >= 40:
        grade.append("C")
    else:
        grade.append("D")

print(grade)