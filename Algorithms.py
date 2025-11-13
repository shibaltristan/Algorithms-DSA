import sys

students = []

def bubble_sort(students, key):
    n = len(students)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if students[j][key] > students[j + 1][key]:
                students[j], students[j + 1] = students[j + 1], students[j]


def binary_search(students, student_id):
    low, high = 0, len(students) - 1
    while low <= high:
        mid = (low + high) // 2
        if students[mid]['id'] == student_id:
            return mid
        elif students[mid]['id'] < student_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade: ")

    if any(s['id'] == sid for s in students):
        print("❌ Student ID already exists!")
        return

    students.append({'id': sid, 'name': name, 'grade': grade})
    print("✅ Student added successfully!")

    print("\n📋 Updated Student List (Sorted by Name):")
    display_students(auto=True)


def edit_student():
    sid = input("Enter ID of student to edit: ")
    sorted_list = sorted(students, key=lambda x: x['id'])
    index = binary_search(sorted_list, sid)

    if index == -1:
        print("❌ Student not found!")
        return

    for s in students:
        if s['id'] == sid:
            print(f"Editing Student: {s}")
            s['name'] = input("Enter new name (leave blank to keep current): ") or s['name']
            s['grade'] = input("Enter new grade (leave blank to keep current): ") or s['grade']
            print("✅ Student updated successfully!")

            print("\n📋 Updated Student List (Sorted by Name):")
            display_students(auto=True)
            return


def delete_student():
    sid = input("Enter ID of student to delete: ")
    for s in students:
        if s['id'] == sid:
            print(f"Found Student: {s}")
            choice = input("Would you like to edit this student before deleting? (y/n): ").lower()
            if choice == 'y':
                edit_student()
            confirm = input("Are you sure you want to delete this student? (y/n): ").lower()
            if confirm == 'y':
                students.remove(s)
                print("🗑️ Student deleted successfully!")

                if students:
                    print("\n📋 Updated Student List (Sorted by Name):")
                    display_students(auto=True)
                else:
                    print("⚠️ No students left in the list.")
            return
    print("❌ Student not found!")


def display_students(auto=False):
    if not students:
        if not auto:
            print("⚠️ No students to display!")
        return

    if not auto:
        print("\nSort by: 1) Name  2) Grade")
        choice = input("Enter choice: ")
        key = 'name' if choice == '1' else 'grade'
    else:
        key = 'name'

    sorted_students = students.copy()
    bubble_sort(sorted_students, key)

    print("\n--- Student List (Sorted by", key.capitalize(), ") ---")
    print("{:<10} {:<20} {:<10}".format("ID", "Name", "Grade"))
    print("-" * 40)
    for s in sorted_students:
        print("{:<10} {:<20} {:<10}".format(s['id'], s['name'], s['grade']))
    print()


def search_student():
    if not students:
        print("⚠️ No students in list!")
        return

    sid = input("Enter Student ID to search: ")

    sorted_students = sorted(students, key=lambda x: x['id'])
    index = binary_search(sorted_students, sid)

    if index != -1:
        print("✅ Student found:", sorted_students[index])
    else:
        print("❌ Student not found!")


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
            print("👋 Exiting program...")
            sys.exit()
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    menu()
