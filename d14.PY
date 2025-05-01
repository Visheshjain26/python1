def student_result():
    sub1 = int(input("Enter marks for subject 1: "))
    sub2 = int(input("Enter marks for subject 2: "))
    sub3 = int(input("Enter marks for subject 3: "))
    
    total = sub1 + sub2 + sub3
    average = total / 3
    
    grades = []
    passed = True
    
    # Function to assign grade based on marks
    def assign_grade(marks):
        if marks == 0:
            return "NA" 
        elif marks <= 39:
            return "F" 
        elif 40 <= marks <= 44:
            return "P"  
        elif 45 <= marks <= 49:
            return "C"  
        elif 50 <= marks <= 54:
            return "B"  
        elif 55 <= marks <= 59:
            return "B+"  
        elif 60 <= marks <= 69:
            return "A" 
        elif 70 <= marks <= 79:
            return "A+" 
        else:
            return "O" 
    
    # Assign grades for each subject
    grades.append(assign_grade(sub1))
    grades.append(assign_grade(sub2))
    grades.append(assign_grade(sub3))
    
    # Check if the student has failed in any subject
    if sub1 <= 39 or sub2 <= 39 or sub3 <= 39:
        passed = False
    
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grades:", grades)
    
    if passed:
        print("Result: Passed")
    else:
        print("Result: Failed")