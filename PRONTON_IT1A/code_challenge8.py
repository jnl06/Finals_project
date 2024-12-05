prelim = eval(input("Enter your prelim grade: "))
midterm = eval(input("Enter your midterm grade: "))
semifinal = eval(input("Enter your semifinal grade: "))
final = eval(input("Enter yur score on final exam: "))
quiz = eval(input("Enter your score on quiz: "))
project = eval(input("Enter your score on project: "))

final_grade = (prelim * 0.15) + (midterm * 0.15) +(semifinal * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)

print(f"Your final grade is {final_grade}")

if final_grade >= 75 :
	print("Congratulations! You passed the course")

else :
	print("Sorry, you failed")