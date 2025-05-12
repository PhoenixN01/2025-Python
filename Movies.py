movies = {
    "M001": {
        "title": "Inception",
        "genre": "Sci-Fi",
        "duration": 148,
        "seats": 85,
        "rating": 6,
        "reviews": {
            1: {"name": "Adam", "rating": 6, "comment": "Amazing plot!"},
        },
        "price": 12,
    },
    "M002": {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "duration": 169,
        "seats": 110,
        "rating": 4.6,
        "reviews": {
            1: {"name": "Jane", "rating": 4.6, "comment": "Mind-expanding!"},
        },
        "price": 13,
    },
    "M003": {
        "title": "Joker",
        "genre": "Drama",
        "duration": 122,
        "seats": 100,
        "rating": 8.0,
        "reviews": {
            1: {"name": "Jason", "rating": 8.0, "comment": "Dark and intense."},
        },
        "price": 12,
    },
}
 
users = {
    "admin": {"password": "unbirvwb"},
    "Billy": {"password": "billy", "balance": 1250.50},
    "Bobby": {"password": "bobby", "balance": 820.00},
    "Bo": {"password": "bo", "balance": 312.75},
}

current_user = ""
logged_in = False


def login(users, current_user, logged_in):
    login_attempts = 0
    yes_answers = ["y", "yes", "yeah", "yep"]
    print("Please Enter Username and Password to begin.")
    while login_attempts < 5:
        username = input("Username: ")
        if username in users:
            password_attempts = 0
            while password_attempts < 5:
                password = input("Password: ")
                if password == users[username]["password"]:
                    print("Login Success")
                    break
                else:
                    print("Password is Incorrect")
                    password_attempts += 1
            if password_attempts == 5:
                print("You have entered your password incorrectly 5 times")
                change_user = input("Would you like to change users?")
                if change_user.lower() in yes_answers:
                    login(users, current_user, logged_in)
                    break
                else:
                    print("Goodbye.")
                    logged_in = False
                    return users, current_user, logged_in
            elif password_attempts < 5:
                current_user = username
                print("Welcome ", current_user)
                logged_in = True
                break
        else:
            print("Username Not Found")
            login_attempts += 1
    if login_attempts == 5:
        print("Login attempt Timeout. Please try again later")
    return users, current_user, logged_in

def search_movies(target, movies=dict):
    title = "title"
    for i in movies:
        if movies[i][title] == target:
            return True

def admin_account(users, movies, current_user):
    if current_user == "admin":
        tasks = ["Add Movie [0]", "Edit Movie [1]", "View User details [2]" "Edit User details [3]", "Return to Main Menu [4]"]
        print("Admin Tasks: ")
        for i in tasks:
            print(i)
        current_task = input("Task id: ")
        
        
    else:
        print("You do not have permission to access this account")
        return

users, current_user, logged_in = login(users, current_user, logged_in)