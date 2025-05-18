def weighted_score(grade, unit):
    return {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}.get(grade, 0) * unit

units = score = 0
courses = int(input("Number of courses: "))

for i in range(courses):
    unit = int(input(f"EIE {i+322} units: "))
    grade = input("Grade (A-F): ").strip().upper()
    score += weighted_score(grade, unit)
    units += unit

gpa = round(score / units, 2) if units else 0
print("Your GPA is:", gpa)