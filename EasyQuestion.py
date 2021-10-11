#
# File        : EasyQuestion.py  
# Created     : 11/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : 
#

if __name__ == '__main__':
    students_numbers = ("L12345", "L54321")
    module_names = ["Java_ooprogramming", "Python Scripting"]
    java_ooprogramming_grades = {"L12345": 40, "L54321": 70}
    python_scripting_grades = {"L12345": 69, "L54321": 58}

    print("We have two students currently enrolled - {}".format(students_numbers))
    selected_student = input("Enter a student: ")
    print("\nStudent Record Search Results\n")

    if selected_student in java_ooprogramming_grades:
        print("Module: {0}\t\tGrade: {1}".format(module_names[0],java_ooprogramming_grades[selected_student]))
    else:
        print("Student not taking the {} module.".format(module_names[0]))

    if selected_student in python_scripting_grades:
        print("Module: {0}\t\tGrade: {1}".format(module_names[1],python_scripting_grades[selected_student]))
    else:
        print("Student not taking the {} module.".format(module_names[1]))

