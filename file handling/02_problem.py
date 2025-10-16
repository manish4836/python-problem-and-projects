# Students ka data file mein save karenge

def add_astudents():
    name = input("students ka name: ")
    age = input("students ki age: ")
    grade = input("students ka grade: ")

    with open("student_data.txt","a") as file:
        file.write(f"{name},{age},{grade}\n")

    print(f"{name} ka data save ho gaya hai!")

def view_students():
    try: 
        with open("student_data.txt", "r") as file:
            print("\n sare students: ")
            print("=" * 30)
            for line in file:
                name, age, grade = line.strip().split(',')
                print(f"name: {name}")
                print(f"age: {age}")
                print(f"grade: {grade}")
                print("-" * 20)

    except FileNotFoundError:
        print(f"Abhi tak koi students ka data nahi hai!")

while True:
    print("\n1. Naya student add karna ")
    print("2. saare students dekhna ")
    print("3. Exit")

    choice = input("Aapka choice bataiye (1-3): ")

    if choice == "1":
        add_astudents()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("wrong input try again!")
