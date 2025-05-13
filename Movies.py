movies = {
    "Inception": {
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
    "Interstellar": {
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
    "Joker": {
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
    for i in movies:
        if movies[i] == target:
            return True

def add_movie(movies=dict):
    while True:
        title = input("Movie Title: ")
        genre = input("Movie Genre: ")
        duration = input("Movie Duration: ")
        seats = input("Seats allocated for Movie: ")
        price = input("Ticket Price for Movie: ")
        print()
        print("New Movie Details: ")
        print("Title: ", title)
        print("Genre: ", genre)
        print("Duration: ", duration)
        print("Number of Seats: ", seats)
        print("Ticket Price: ", price)
        while True:
            confirmation = input("Cofirm? (y/n): ")
            if confirmation == "y":
                movies[title] = {"title": title, "genre": genre, "duration": duration, "seats": seats, "ratings": {}, "price": price}
                print()
                print("Returning to the admin menu now. ")
                print()
                return movies
            elif confirmation == "n":
                retry = input("Would you like to try again? (y/n): ")
                if retry == "y":
                    break
                elif retry == "n":
                    print()
                    print("Returning to the admin menu now. ")
                    print()
                    return movies
                else:
                    print("Invalid Response")
            else:
                print("Invalid Response")

    
def edit_movie(movies=dict):
    count = 0
    while True:
        target = input("Movie to Edit: ")
        if target in movies.keys():
            print(target, " Selected.")
            print("Movie Details: ")
            title = "title"
            print("[0] Title: ", movies[target][title])
            genre = "genre"
            print("[1] Genre: ", movies[target][genre])
            duration = "duration"
            print("[2] Duration: ", movies[target][duration])
            seats = "seats"
            print("[3] Seats: ", movies[target][seats])
            reviews = "reviews"
            print("[4] Reviews", movies[target][reviews])
            price = "price"
            print("[5] Price: ", movies[target][price])
            options = [title, genre, duration, seats, reviews, price]
            while True:
                selection = input("Item to edit [0-5]. [EXIT] to cancel: ")
                if selection.isdigit():
                    selection = int(selection)
                    if selection in range(0, 6):
                        change_id = options[selection]
                        change = input(f"What would you like {change_id} to be? ")
                        movies[target][change_id] = change
                        print("Change Successful")
                        print()
                        print("Returning to the Admin Menu Now.")
                        print()
                        return movies
                    else:
                        print("Item Not Found")
                elif selection == "EXIT":
                    return movies
                else:
                    print("Invalid Item Id")
        else:
            print("Movie Not Found")
            count += 1
        if count == 3:
            exit = input("Would you like to return to the admin menu? (y/n)")
            if exit == "y":
                print()
                print("Returning to the Admin Menu Now.")
                print()
                return movies
            elif exit == "n":
                count = 0
                continue
            else:
                print("Invalid Response")


# def view_users(users=dict):

# def edit_users(users=dict):

def admin_account(users, movies, current_user):
    if current_user == "admin":
        while True:
            tasks = ["Add Movie [0]", "Edit Movie [1]", "View User details [2]", "Edit User details [3]", "Return to Main Menu [4]"]
            print("Admin Tasks: ")
            for i in tasks:
                print(i)
            current_task = 0
            while True:
                current_task = input("Task id: ")
                if current_task.isdigit():
                    current_task = int(current_task)
                    if current_task in range(0, 5):
                        break
                    else:
                        print("Task Id Not Found")
                else:
                    print("Invalid Task Id")

            if current_task == 0:
                movies = add_movie(movies)
            elif current_task == 1:
                movies = edit_movie(movies)
            # elif current_task == 2:
                # users = view_users(users)
            # elif current_task == 3:
                # users = edit_users(users)
            else:
                return
    else:
        print("You do not have permission to access this account")
        return

users, current_user, logged_in = login(users, current_user, logged_in)
admin_account(users, movies, current_user)