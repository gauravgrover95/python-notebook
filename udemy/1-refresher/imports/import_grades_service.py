def calculate_homework(hw_grades: dict):
    grades_sum = 0
    for hw, grade in hw_grades.items():
        grades_sum += grade
    final_grade = grades_sum / len(hw_grades)
    final_grade = round(final_grade, 2)
    print('final_grade', final_grade)
    return final_grade


# These statements execute, once the module is imported.
# These are intended to initialize the module only
print('hello from executables in grading service')

something = 'new'