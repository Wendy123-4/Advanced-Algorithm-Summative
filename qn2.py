def gradingStudents(grades):
    # set the input list of grades as the original grades
    original = grades
    # instantiate counter that loops through the grades list
    i = 0
    # Implementing the constraints
    # Number of students >= 1 but <= 60 ,
    # the number of grades represents the number of students
    # The grades must be <= 100 but >= 0
    while 1 <= len(grades) <= 60 and 0 <= grades[i] <= 100:

        # the list stores the rounded off grades
        rounded_grades = []

        # iterating each grade in the list to meet grading policy
        for i in grades:

            # if less than 38 no rounding off
            # or difference with next multiple of 5 2 or less no rounding off
            if i < 38 or i % 5 <= 2:
                rounded_grades.append(i)
            else:
                # once difference with next multiple of 5 3 or more,
                # round off to next multiple
                i += 5 - (i % 5)
                rounded_grades.append(i)
        # return original grade against final grade
        return "Original Grades: " + str(original) + "\n" + "Final Grades: " + str(rounded_grades)


# Testing
print(gradingStudents([73, 67, 38, 33]))
