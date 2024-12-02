def code_chal6():
    prelim = eval(input("Enter your prelim grade: "))
    midterm = eval(input("Enter your midterm grade: "))
    semifinal = eval(input("Enter your semifinal grade: "))
    final = eval(input("Enter your final grade: "))
    quiz = eval(input("Enter your quiz grade: "))
    project = eval(input("Enter your project grade: "))

    if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100 ) and (semifinal >= 65 and semifinal <= 100) and (final >= 65 and final <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100) : 
        final_grade = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)
    
        print(f"Your final grade is {final_grade}")
        if final_grade >= 75 :
            print("Congratulations! You passed the course")
    
        else :
            print("Sorry, you failed")
    
    else :
        print("Invalid Grade")    