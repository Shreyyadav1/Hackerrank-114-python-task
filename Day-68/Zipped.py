# Step 1: Read number of students and subjects
n, x = map(int, input().split())

# Step 2: Store marks of each subject
marks = []

for i in range(x):

    # Read marks for one subject
    subject_marks = list(map(float, input().split()))

    marks.append(subject_marks)

# Step 3: zip(*) converts subject-wise data
# into student-wise data
students = zip(*marks)

# Step 4: Calculate average for each student
for student in students:

    average = sum(student) / len(student)

    print(average)