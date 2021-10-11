#
# File        : FollowAlong.py  
# Created     : 07/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Following along with today's course notes
#

from copy import deepcopy

if __name__ == '__main__':
    empty_list = []
    empty_list.append(10)
    ages = [19, 21, 20]

    student1_details = [20, "Michael Brennan", 77.5]
    student2_details = [33, "Mairead Gallagher", 65]

    class_of_students = [student1_details, student2_details, "module title", [2, 3, 4]]
    group_of_students = student1_details + student2_details

    print(" {} ".format(ages[1]))
    print(" {0} \t\t{1} \t{2} ".format(student1_details[0], student1_details[1], student2_details[2]))
    print(" {} ".format(student1_details))
    print(" {} ".format(class_of_students))
    print(" {} ".format(class_of_students[0][1]))

    books = []

    '''
    for i in range (0, 4):
        books.append(input("Enter Detail: "))
    
    for i in range (0, 4):
        print("{0} has a value of 1".format(i, books[i]))
    '''

    ages[1] = 33
    print("{}\n".format(ages[1]))

    group_of_students = class_of_students[0:2]
    print(group_of_students)
    print("1st student, 2nd datum is: {0}".format(group_of_students[0][1]))

    second_group_of_students = student1_details + student2_details
    third_group_of_students = []
    third_group_of_students += second_group_of_students

    print("Is Michael in list? {}".format(("Michael" in group_of_students[0][1])))
    print("Is Michael in list? {}".format(("Michael" in group_of_students[0])))

    grades = [1,2,3]
    #nu_grades = [grades] * 2
    #print("{}".format(nu_grades))

    #nu_grades[0][0] = 6
    #print("Repeated list after change {}".format(nu_grades))

    my_range = list(range(1,5))
    print(my_range)

    stu_grades = [['L12345', 45, 61],
                  ['L54321', 40, 70]]

    print("LNum: {}".format(stu_grades[0][0]))
    print("Grade 1: {}".format(stu_grades[0][1]))

    student3_details = student2_details
    print("Student 2 Details: {}".format(student2_details))
    print("Student 3 Details: {}".format(student3_details))

    student3_details[0] = 44
    print("\n After Change: ")
    print("Student 2 Details {0}, with id of {1}".format(student2_details, id(student2_details)))
    print("Student 3 Details {0}, with id of {1}".format(student3_details, id(student3_details)))

    student4_details = student2_details[:]
    student5_details = deepcopy(student2_details)

    student4_details[0]=999
    student5_details[0] = 88

    print("\n After Slice: ")
    print("Student 4 Details {0}, with id of {1}".format(student4_details, id(student4_details)))
    print("\n After Deepcopy: ")
    print("Student 5 Details {0}, with id of {1}".format(student5_details, id(student5_details)))

    empty_tuple = ()
    grades = (40,50,60)
    student1_python_exam = ("L0012345", "Michael Brennan", 77.5)
    student2_python_exam = ("L0055442", "Mairead Gallagher", 65)
    python_class_of_students = [student1_python_exam, student2_python_exam, "Python", [10, 11, 12]]

    print("\nTuples Examples\n")
    print("{}".format(grades[1]))
    print("{0} \t\t{1} \t{2}".format(student1_python_exam[0], student1_python_exam[1], student1_python_exam[2]))
    print("item in embedded tuple: {}".format(python_class_of_students[0][2]))
    print("item in unnamed list: {}".format(python_class_of_students[3][2]))

    list_of_contents = list(empty_tuple)
    list_of_contents.append("New Element")
    empty_tuple = tuple(list_of_contents)
    print("Updated list \n{}".format(list_of_contents))
    print("Updated tuple \n{}".format(empty_tuple))
    print(len(empty_tuple))

    campuses = {}
    contacts = {"Ruth Lennon": 749186355, "Thomas Dowling": 749186304, "Killybegs Reception": 749186600}
    contacts_addr = {"Ruth Lennon": "Port Road", "Thomas Dowling": "Port Road", "Killybegs Reception": "Killybegs Campus"}
    print(contacts)
    print(contacts_addr)

    print(contacts["Ruth Lennon"])

    contacts["Karen Doherty"] = 7419186306
    campuses["Port Road"] = "Port Road, Letterkenny"
    campuses["Killybegs"] = "Shore Rd., Killybegs"
    campuses["BDC"] = "Port Road, Letterkenny"

    print(contacts)
    print(campuses)

    print(len(campuses))
    del campuses["BDC"]
    print(len(campuses))

    print("Killybegs" in campuses)

    campuses["Ramelton Rd"] = "Ramelton Rd., Letterkenny"
    print("\nPop Example:\n{}".format(campuses))
    campus_name, campus_address = campuses.popitem()
    print("Name is: {0} and address is: {1}".format(campus_name, campus_address))
    print("\nAfter pop\n{}".format(campuses))

    if "Port Road" in campuses:
        print(campuses["Port Road"])

    campuses.get("MPC")

    computing_contacts = contacts.copy()
    comp_staff_copy = deepcopy(contacts)

    emg_staff_contacts = {"Dennis McFadden": 749186402}
    all_staff_contacts = {}
    all_staff_contacts.update(emg_staff_contacts)
    all_staff_contacts.update(comp_staff_copy)
    print(all_staff_contacts)

    for key in all_staff_contacts:
        print(key)

    staff = all_staff_contacts.keys()
    phone = all_staff_contacts.values()
    nu_list = all_staff_contacts.items()

    design_staff = ["Nollaig", "Kelda"]
    design_phones = [9186123, 9186281]
    design_contact_list = (list(zip(design_staff, design_phones)))
    print("List of tuples: {}".format(design_contact_list))
    design_cont_dict = dict(design_contact_list)
    print("Dictionary: {}".format(design_cont_dict))

    class_group_1 = {"Pat": 12345, "Priyank": 54321}
    class_group_2 = {"Jo": 12222, "Muhammed": 55555 }
    full_class = class_group_1 | class_group_2
    print(full_class)

    full_class |= {"Xiao Xiao": 32321}
    full_class |= {"Pat": 11234}
    print(full_class)

