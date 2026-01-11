"""
- Modules get used all the time throughout programming
- It helps with creating more files, with unique purpose, to help with clean maintainable code
"""

import import_grades_service as grade_service

hw_grades = {
    'hw_1': 85,
    'hw_2': 100,
    'hw_3': 81
}


final_grade = grade_service.calculate_homework(hw_grades)

print(grade_service.something)