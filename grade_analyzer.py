def get_valid_grade(student_name):
    try:
        grade = float(input(f"Enter grade for {student_name} (0-100): "))
        if 0 <= grade <= 100:
            return grade
        else:
            print("Grade must be between 0 and 100. Try again.")
            return get_valid_grade(student_name)
    except ValueError:
        print("Invalid input. Enter a number.")
        return get_valid_grade(student_name)

def display_student_summary(names, grades):
    print("\nStudent Summary:")
    for i in range(len(names)):
        print(f"{names[i]}: {grades[i]}")

def get_avg_grade(grades):
    return sum(grades) / len(grades)

def get_heighest_grade(names, grades):
    max_grade = max(grades)
    index = grades.index(max_grade)
    return names[index], max_grade

def count_passed(grades):
    return sum(1 for grade in grades if grade >= 60)

def main():
    try:
        num_students = int(input("Enter number of students: "))
        if num_students <= 0:
            print("Number must be greater than 0.")
            return main()
    except ValueError:
        print("Invalid input. Enter a number.")
        return main()

    student_names = []
    student_grades = []

    for i in range(num_students):
        name = input(f"\nEnter name for student #{i+1}: ")
        grade = get_valid_grade(name)
        student_names.append(name)
        student_grades.append(grade)

    display_student_summary(student_names, student_grades)
    avg = get_avg_grade(student_grades)
    top_student, top_grade = get_heighest_grade(student_names, student_grades)
    passed_count = count_passed(student_grades)

    print(f"\nClass average: {avg:.2f}")
    print(f"Top student: {top_student} with grade {top_grade}")
    print(f"Number of students who passed: {passed_count}")

main()
