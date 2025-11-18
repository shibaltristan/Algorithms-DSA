import sys

students_TLS = []

def bubble_sort(students_TLS, key):
    n = len(students_TLS)
    for i in range(n - 1):
        for j in range(n - i - 1):
            a = students_TLS[j][key]
            b = students_TLS[j + 1][key]

            # Convert grade to int for numerical sorting
            if key == 'grade':
                a = int(a)
                b = int(b)

            if a > b:
                students_TLS[j], students_TLS[j + 1] = students_TLS[j + 1], students_TLS[j]

def binary_search(students_TLS, student_id):
    low, high = 0, len(students_TLS) - 1
    while low <= high:
        mid = (low + high) // 2
        if students_TLS[mid]['id'] == student_id:
            return mid
        elif students_TLS[mid]['id'] < student_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade: ")

    if any(s['id'] == sid for s in students_TLS):
        print(" Student ID already exists!")
        return

    # Store grade as integer
    students_TLS.append({'id': sid, 'name': name, 'grade': int(grade)})
    print(" Student added successfully!")

    print("\n Updated Student List (Sorted by Grade):")
    display_students(auto=True, sort_key='grade')

def edit_student():
    sid = input("Enter ID of student to edit: ")
    sorted_list = sorted(students_TLS, key=lambda x: x['id'])
    index = binary_search(sorted_list, sid)

    if index == -1:
        print(" Student not found!")
        return

    for s in students_TLS:
        if s['id'] == sid:
            print(f"Editing Student: {s}")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_grade = input("Enter new grade (leave blank to keep current): ")

            if new_name:
                s['name'] = new_name
            if new_grade:
                s['grade'] = int(new_grade)

            print(" Student updated successfully!")

            print("\n Updated Student List (Sorted by Grade):")
            display_students(auto=True, sort_key='grade')
            return

def delete_student():
    sid = input("Enter ID of student to delete: ")
    for s in students_TLS:
        if s['id'] == sid:
            print(f"Found Student: {s}")
            choice = input("Would you like to edit this student before deleting? (y/n): ").lower()
            if choice == 'y':
                edit_student()
            confirm = input("Are you sure you want to delete this student? (y/n): ").lower()
            if confirm == 'y':
                students_TLS.remove(s)
                print(" Student deleted successfully!")

                if students_TLS:
                    print("\n Updated Student List (Sorted by Grade):")
                    display_students(auto=True, sort_key='grade')
                else:
                    print(" No students left in the list.")
            return
    print(" Student not found!")

def display_students(auto=False, sort_key='name'):
    if not students_TLS:
        if not auto:
            print(" No students to display!")
        return

    if not auto:
        print("\nSort by: 1) Name  2) Grade")
        choice = input("Enter choice: ")
        sort_key = 'name' if choice == '1' else 'grade'

    sorted_students = students_TLS.copy()
    bubble_sort(sorted_students, sort_key)

    print(f"\n--- Student List (Sorted by {sort_key.capitalize()}) ---")
    print("{:<10} {:<20} {:<10}".format("ID", "Name", "Grade"))
    print("-" * 40)
    for s in sorted_students:
        print("{:<10} {:<20} {:<10}".format(s['id'], s['name'], s['grade']))
    print()

def search_student():
    if not students_TLS:
        print(" No students in list!")
        return

    sid = input("Enter Student ID to search: ")

    sorted_students = sorted(students_TLS, key=lambda x: x['id'])
    index = binary_search(sorted_students, sid)

    if index != -1:
        print(" Student found:", sorted_students[index])
    else:
        print(" Student not found!")

def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Edit Student")
        print("3. Delete Student")
        print("4. Display Students (Sorted)")
        print("5. Search Student by ID (Binary Search)")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            edit_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            display_students()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print(" Exiting program...")
            sys.exit()
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    menu()
