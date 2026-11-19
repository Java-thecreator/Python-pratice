students = []

while True:

    print("================================================")
    print("         STUDENT GRADE MANAGER                  ")
    print("================================================")

    print("Welcome to the Student Grade Manager")

    print("\nMain Menu")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4.  Calculate Grade ")
    print("5. Exit")

    choice = input("\nEnter any option: ")

    print("You selected option:", choice)

    # OPTION 1: ADD STUDENT
    if choice == "1":

        student_name = input("Enter your full name: ")

        try:
            student_score = int(input("Enter your score: "))

            if student_score < 0 or student_score > 100:
                print("Invalid score! Enter a score between 0 and 100.")

            else:

                # Calculate Grade
                if student_score >= 80:
                    grade = "A"
                elif student_score >= 70:
                    grade = "B"
                elif student_score >= 60:
                    grade = "C"
                elif student_score >= 50:
                    grade = "D"
                else:
                    grade = "F"

                # Create Student Dictionary
                student = {
                    "name": student_name,
                    "score": student_score,
                    "grade": grade
                }

                # Store Student
                students.append(student)

                print("\nStudent added successfully!")
                print("Name:", student_name)
                print("Score:", student_score)
                print("Grade:", grade)

        except ValueError:
            print("Invalid input! Please enter a numerical score.")

    # OPTION 2: VIEW STUDENTS
    elif choice == "2":
        if not students:
            print("No students registered yet")
        else:
            print("=======Registered Students=========")
            for index, student in enumerate(students, start=1):
                print(f"Student {index}")
                print("Name:", student["name"])
                print("Score:", student["score"])    
                print("Grade:", student["grade"])  
                print("\n================================================")       
 
    # OPTION 3: SEARCH STUDENT
    elif choice == "3":
        search_name=input("Enter the name of student to search: ")
        found = False
        for student in students:
           
            if student["name"].lower()==search_name.lower():
                found=True
                print("Name:", student["name"])
                print("Score:", student["score"])    
                print("Grade:", student["grade"]) 
                break
        if not found:    
            print("Student not found")

    # OPTION 4: CALCULATE GRADE
    elif choice == "4":
        print("Search Student")

    # OPTION 5: EXIT
    elif choice == "5":
        print("Thank you for using Student Grade Manager!")
        break

    # INVALID MENU OPTION
    else:
        print("Invalid option! Please select between 1 and 5.")