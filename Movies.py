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

def login(users):
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
                    login(users)
                    break
                else:
                    print("Goodbye.")
                    return
            elif password_attempts < 5:
                print("Welcome")
                break
        else:
            print("Username Not Found")
            login_attempts += 1
    if login_attempts == 5:
        print("Username Not Found.")
        add_user = input("Would you like to create an account instead?")
        if add_user.lower() in yes_answers:
            # signup()
            print("signup")
    return

            
        
        
                

login(users)