def get_valid_name():
    name = input("Enter student name (letters only): ")
    if name.replace(" ", "").isalpha():
        return name
    else:
        print("Invalid name. Please use letters only with no numbers or symbols.")
        return get_valid_name()

def get_valid_grade(student_name):
    grade_input = input(f"Enter grade for {student_name} (0-100): ")
    if grade_input.replace('.', '', 1).isdigit():
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return grade
        else:
            print("Grade must be between 0 and 100. Try again.")
            return get_valid_grade(student_name)
    else:
        print("Invalid input. Please enter a number.")
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
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count

def main():
    num_input = input("Enter number of students: ")
    if not num_input.isdigit() or int(num_input) <= 0:
        print("Please enter a positive whole number.")
        return main()

    num_students = int(num_input)
    student_names = []
    student_grades = []

    for i in range(num_students):
        print(f"\nStudent #{i+1}")
        name = get_valid_name()
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

