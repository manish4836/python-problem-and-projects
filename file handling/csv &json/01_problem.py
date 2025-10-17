import csv
import json

def display_menu():
    print("\n" + "="*50)
    print("           STUDENT DATA MANAGER")
    print("="*50)
    print("1. Add Student to CSV")
    print("2. View All Students from CSV")
    print("3. Add Student to JSON")
    print("4. View Student from JSON")
    print("5. Exit")
    print("="*50)

def add_student_csv():
    print("\n--- Add Student to CSV ---")
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    city = input("Enter city: ")
    
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade, city])
    
    print(f"✅ {name} CSV mein add ho gaya!")

def view_students_csv():
    print("\n--- All Students from CSV ---")
    try:
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(f"Name: {row[0]}, Age: {row[1]}, Grade: {row[2]}, City: {row[3]}")
    except FileNotFoundError:
        print("❌ CSV file nahi mili! Pehle koi student add karein.")

def add_student_json():
    print("\n--- Add Student to JSON ---")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    city = input("Enter city: ")
    
    student_data = {
        "name": name,
        "age": age,
        "grade": grade,
        "city": city
    }
    
    with open('student_data.json', 'w') as file:
        json.dump(student_data, file, indent=4)
    
    print(f"✅ {name} JSON file mein save ho gaya!")

def view_student_json():
    print("\n--- Student from JSON ---")
    try:
        with open('student_data.json', 'r') as file:
            data = json.load(file)
            print(f"Name: {data['name']}")
            print(f"Age: {data['age']}")
            print(f"Grade: {data['grade']}")
            print(f"City: {data['city']}")
    except FileNotFoundError:
        print("❌ JSON file nahi mili! Pehle koi student add karein.")

# Main program
def main():
    print("🎉 Student Data Manager Started!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student_csv()
        elif choice == '2':
            view_students_csv()
        elif choice == '3':
            add_student_json()
        elif choice == '4':
            view_student_json()
        elif choice == '5':
            print("👋 Program band ho raha hai. Shukriya!")
            break
        else:
            print("❌ Galat choice! Phir se try karein.")

# Program start
if __name__ == "__main__":
    main()