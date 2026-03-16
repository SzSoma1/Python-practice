student_scores = [180, 122, 144, 12, 148, 166, 155, 199, 140, 125]

total_exam_score = sum(student_scores)
print(total_exam_score)

##sum with loop
all_score = 0
for score in student_scores:
    all_score += score
print(all_score)

print(max(student_scores))

##max with loop
max_score = 0
for score in student_scores:
    if score >= max_score:
        max_score = score
print(max_score)