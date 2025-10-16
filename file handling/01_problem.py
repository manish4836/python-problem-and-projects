# Ek personal diary banayenge jo roz ke thoughts save karegi

def add_diary_entry():
    entry = input("Aaj apna kya thought likhna chahenge? ")
    with open("diary.txt", "a") as diary:
        import datetime
        today = datetime.datetime.now()
        diary.write(f"{today} : {entry}\n")
        print("your thought is save in diary.")

def read_diary():
    try:
        with open("diary.txt", "r") as diary:
            print("\n Aapki diary: ")
            print("=" * 50)
            print(diary.read())
    except FileNotFoundError:
        print("Abhi tak koi entry nahi hai, pahle kuch likhiye")

while True:
    print("\n1. Naya thought likhna ")
    print("2. Diary padhna ")
    print("3. Exit")

    choice = input("Apna choice bataiye (1-3): ")

    if choice == '1':
        add_diary_entry()
    elif choice == '2':
        read_diary()
    elif choice == '3':
        print("Diary band ho rahi hai. Shukriya!")
        break
    else:
        print("Galat choice! Phir se try kariye.")