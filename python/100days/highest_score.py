# ------------------------------------
# From Angela Yu's "100 Days of Code"
# ------------------------------------

# Highest score
student_scores = input("Input a list of student scores separated by a space: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest = 0
for n in range(0, len(student_scores)):
    if student_scores[n] > highest:
        highest = student_scores[n]

print(f"The highest score is: {highest}")