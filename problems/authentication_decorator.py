def is_admin(func):
    user_is_authenticated = True

    def wrapper():
        if user_is_authenticated:
            print("✅ Access Granted!")
            return func()
        else:
            print("❌ Access Denied: Please log in.")
    return wrapper
@is_admin
def show_secret_data():
    return "SERVER DATA: Balance is 1,000,000 INR."

result = show_secret_data()
print(f"Function Output: {result}")