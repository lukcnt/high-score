student_scores = input("Input a list of student scores with a space between each one : ").split()

# Didn't use max function purposely to get a better grasp of for loops.
highest_score = 0

for score in student_scores:
    if int(score) > highest_score:
        highest_score = int(score)

print(f"The highest score in the class is: {highest_score}.")