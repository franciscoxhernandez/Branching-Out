import json

def filter_users_by_name(name):
    with open("user.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    with open("user.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["age"] == age]
    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    print(f"Searching for: {email.lower()}")  # Debug
    try:
        with open("user.json", "r") as file:
            users = json.load(file)
        print(f"Loaded {len(users)} users")  # Debug
        filtered_users = [user for user in users if user["email"].lower() == email.lower()]
        if filtered_users:
            for user in filtered_users:
                print(user)
        else:
            print("No users found with that email.")
    except FileNotFoundError:
        print("ERROR: users.json file not found.")
    except json.JSONDecodeError:
        print("ERROR: users.json file is not valid JSON.")

def main():
    filter_option = input("What would you like to filter by? (name, age, or email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_search)
        except ValueError:
            print("Invalid age. Please enter a number.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")

if __name__ == "__main__":
    main()
