# Programmer: James E Johnson
# Program: Assignment 1, Phase 2
# Date: March 13, 2021
# Version: 2.7


# Constants

curr_semester = input("Enter current semester: ")                         # Current Semester
s_last_name = input("Enter your last name: ")                             # Student Last Name
s_first_name = input("Enter your first name: ")                           # Student First Name
s_banner_id = int(input("Enter your Banner ID: "))                        # Student Banner ID

course_id_1 = input("Enter your first Course's ID : ")                    # String
course_id_2 = input("Enter your second Course's ID : ")                   # String
course_id_3 = input("Enter your third Course's ID : ")                    # String

min_hrs = 1
max_hrs = 5
min_grade = 0.0
max_grade = 4.0

do_again = 'y'

while do_again == 'y' or do_again == 'Y':

    good_data = True
    while good_data:
        if good_data:
            credit_hrs_1 = int(input("Enter your first Course's Credit Hours: "))     # Integer 1-5
            good_data = min_hrs <= credit_hrs_1 <= max_hrs
            if not good_data:
                print('\n ***INVALID CREDIT HOURS *** \n')
        if good_data:
            credit_hrs_2 = int(input("Enter your second Course's Credit Hours: "))     # Integer 1-5
            good_data = min_hrs <= credit_hrs_2 <= max_hrs
            if not good_data:
                print('\n ***INVALID CREDIT HOURS *** \n')
        if good_data:
            credit_hrs_3 = int(input("Enter your third Course's Credit Hours: "))     # Integer 1-5
            good_data = min_hrs <= credit_hrs_3 <= max_hrs
            if not good_data:
                print('\n ***INVALID CREDIT HOURS *** \n')
        if good_data:
            num_grade_1 = float(input("Enter your first Course's number grade: "))     # Integer 1-5
            good_data = min_grade <= num_grade_1 <= max_grade
            if num_grade_1 <= 4.0 and num_grade_1 >= 0.0:
                if num_grade_1 >= 3.5:
                    letter_grade_1 = "A"
                elif num_grade_1 >= 2.5:
                    letter_grade_1 = "B"
                elif num_grade_1 >= 1.5:
                    letter_grade_1 = "C"
                elif num_grade_1 >= 1.0:
                    letter_grade_1 = "D"
                elif num_grade_1 >= 0.0:
                    letter_grade_1 = "F"
            else:
                print('\n *** INVALID NUMBER GRADE *** \n')

        if good_data:
            num_grade_2 = float(input("Enter your second Course's number grade: "))     # Integer 1-5
            good_data = min_grade <= num_grade_2 <= max_grade
            if num_grade_2 <= 4.0 and num_grade_2 >= 0.0:
                if num_grade_2 >= 3.5:
                    letter_grade_2 = "A"
                elif num_grade_2 >= 2.5:
                    letter_grade_2 = "B"
                elif num_grade_2 >= 1.5:
                    letter_grade_2 = "C"
                elif num_grade_2 >= 1.0:
                    letter_grade_2 = "D"
                elif num_grade_2 >= 0.0:
                    letter_grade_2 = "F"
            else:
                print('\n *** INVALID NUMBER GRADE *** \n')
                
        if good_data:
            num_grade_3 = float(input("Enter your third Course's number grade: "))     # Integer 1-5
            good_data = min_grade <= num_grade_3 <= max_grade
            if num_grade_3 <= 4.0 and num_grade_3 >= 0.0:
                if num_grade_3 >= 3.5:
                    letter_grade_3 = "A"
                elif num_grade_3 >= 2.5:
                    letter_grade_3 = "B"
                elif num_grade_3 >= 1.5:
                    letter_grade_3 = "C"
                elif num_grade_3 >= 1.0:
                    letter_grade_3 = "D"
                elif num_grade_3 >= 0.0:
                    letter_grade_3 = "F"
            else:
                print('\n *** INVALID NUMBER GRADE *** \n')
                
        if good_data:   # Placeholder?
            grade_pt_1 = credit_hrs_1 * num_grade_1         
            grade_pt_2 = credit_hrs_2 * num_grade_2         
            grade_pt_3 = credit_hrs_3 * num_grade_3         

            GPA = (grade_pt_1 + grade_pt_2 + grade_pt_3) / (credit_hrs_1 + credit_hrs_2 + credit_hrs_3)
        
            print()
            print()

            # Display Output

            print(' '*15,'Gateway Community College')
            print(' '*22,'Grade Report')
            print(' '*25,curr_semester)
            print('='*55)
            print('Banner ID: ', s_banner_id)
            print('Student Name: ', s_first_name, s_last_name)
            print('='*55)
            print(' '*5, 'Course ID', ' '*5, 'Credit Hours', ' '*5, 'Letter Grade')
            print(' '*5, course_id_1, ' '*13, credit_hrs_1, ' '*16, letter_grade_1)
            print(' '*5, course_id_2, ' '*13, credit_hrs_2, ' '*16, letter_grade_2)
            print(' '*5, course_id_3, ' '*13, credit_hrs_3, ' '*16, letter_grade_3)
            print('='*55)
            print("Student's Current GPA: ", GPA)
            print('='*55)

        do_again = input('Would you like to restart the program? (y/n): ')
        if do_again == 'y' or do_again == 'Y':
            print()
            print('\nProgram Restarted!\n')
            print()
            
        if do_again == 'n' or do_again == 'N':
            print("\nGoodbye!\n")
            break
            
