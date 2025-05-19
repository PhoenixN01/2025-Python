import easygui

movies = {
    "Inception": {
        "Title": "Inception",
        "Genre": "Sci-Fi",
        "Duration": 148,
        "Seats": 85,
        "Rating": 6,
        "Reviews": {
            1: {"name": "Adam", "rating": 6, "comment": "Amazing plot!"},
        },
        "Price": 12,
    },
    "Interstellar": {
        "Title": "Interstellar",
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
        "Title": "Joker",
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
    "admin": {"password": "unbirvwb", "balance": 999999999999.99},
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

def search_movies(movie_id, movies):
    found = False
    for i in movies:
        if movies[i] == movie_id:
            print(movie_id, " Found", sep="")
            print(movies[movie_id])
            found = True
    if found == False:
        print("Movie Not Found")
    return movie_id, movies

def buy_ticket(users, movies, current_user):
    print("Available Movies:")
    for movie in movies.keys():
        print(movie)
    while True:
        selection = input("Which movie would you like to purchase tickets for? ")
        if selection in movies.keys():
            seats_available = int(movies[selection]["Seats"])
            ticket_price = int(movies[selection]["Price"])
            user_balance = users[current_user]["Balance"]
            if seats_available > 0:
                while True:
                    seats_wanted = input("How many seats would you like to purchase? ")
                    if seats_wanted.isdigit():
                        seats_wanted = int(seats_wanted)
                        if seats_wanted <= seats_available:
                            booking_price = seats_wanted * ticket_price
                            if user_balance >= booking_price:
                                user_balance -= booking_price
                                seats_available -= seats_wanted
                                print("Purchase Successful")
                                print("Would you like to purchase some more tickets?")
                                movies[selection]["Seats"] = seats_available
                                users[current_user]["Balance"] = user_balance
                            else:
                                print(f"You have insufficient Funds, you need ${booking_price} to book this amount of seats. Current Balance: ${user_balance}")
                                exit = input("Would you like to try again? (y/n)")
                                if not exit == "y":
                                    break
                        else:
                            print(f"There are only {seats_available} seats available")
                    else:
                        print("Purchase Amount must be an Integer")
            else:
                retry = input("Unfortunately, this movie is already booked out. Would you like to purchase tickets for another movie? (y/n)")
                if retry == "n":
                    break
        else:
            print("Movie Not Found")
    return users, movies

def add_movie(movies):
    while True:

        movie_title = input("Movie Title: ")
        movie_genre = input("Movie Genre: ")
        movie_duration = input("Movie Duration: ")
        movie_seats = input("Seats allocated for Movie: ")
        movie_price = input("Ticket Price for Movie: ")
        print()
        print("New Movie Details: ")
        print("Title: ", movie_title)
        print("Genre: ", movie_genre)
        print("Duration: ", movie_duration)
        print("Number of Seats: ", movie_seats)
        print("Ticket Price: ", movie_price)
        while True:
            confirmation = input("Cofirm? (y/n): ")
            if confirmation == "y":
                movies[movie_title] = {"Title": movie_title, "Genre": movie_genre, "Duration": movie_duration, "Seats": movie_seats, "Rating": 0, 'Reviews': {}, "price": movie_price}
                return movies
            elif confirmation == "n":
                retry = input("Would you like to try again? (y/n): ")
                if retry == "y":
                    break
                elif retry == "n":
                    return movies
                else:
                    print("Invalid Response")
            else:
                print("Invalid Response")

def edit_movie(movies):
    count = 0
    while True:
        target = input("Movie to Edit: ")
        if target in movies.keys():
            print(target, " Selected.")
            print("Movie Details: ")
            print("[0] Title: ", movies[target]["Title"])
            print("[1] Genre: ", movies[target]["Genre"])
            print("[2] Duration: ", movies[target]["Duration"])
            print("[3] Seats: ", movies[target]["Seats"])
            print("[4] Rating: ", movies[target]["Rating"])
            print("[5] Reviews: ", movies[target]["Reviews"])
            print("[6] Price: ", movies[target]["Price"])
            options = ["Title", "Genre", "Duration", "Seats", "Reviews", "Price"]
            while True:
                selection = input("Item to edit [0-5]. [EXIT] to cancel: ")
                if selection.isdigit():
                    selection = int(selection)
                    if selection in range(0, 6):
                        change_id = options[selection]
                        change = input(f"What would you like {change_id} to be? ")
                        movies[target][change_id] = change
                        print("Change Successful")
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
                return movies
            elif exit == "n":
                count = 0
                continue
            else:
                print("Invalid Response")

def view_users(users):
    print("Here are the current list of users")
    user_display = list(users.keys())
    user_display.pop(0)
    for user in user_display:
        print(user, ": ", users[user], sep="")
    goto_edit_users = input("Would you like to edit this list? (y/n)")
    if goto_edit_users == "y":
        users = edit_users(users)
        return users
    else:
        return users

def edit_users(users):
    while True:
        user = input("Which user would you like to edit: ")
        user_info = users[user]
        if user in users.keys():
            for item in user_info.keys():
                print(item, ": ", user_info[item], sep="")
            while True:
                change_id = input(f"What would you like to edit on {user}'s profile? ")
                if change_id in user_info.keys():
                    change = input(f"What would you like to change {change_id} to? ")
                    user_info[change_id] = change
                    print("Changing Detail Now.")
                    repeat = input("Is there any other changes you would like to make? (y/n)")
                    if repeat == "n":
                        break
                else:
                    print("Invalid item")
        else:
            print("User Not Found")
        users[user] = user_info
        return users


def admin_account(users, movies):
    while True:
        tasks = ["Add Movie [0]", "Edit Movie [1]", "View User details [2]", "Edit User details [3]", "Return to Main Menu [4]"]
        print("Admin Tasks: ")
        for i in tasks:
            print(i)
        current_task = 0
        task_list = [add_movie, edit_movie, view_users, edit_users]
        task_inputs = [movies, movies, users, users]
        while True:
            current_task = input("Task id: ")
            if current_task.isdigit():
                current_task = int(current_task)
                if current_task in range(0, 4):
                    break
                elif current_task == 4:
                    return users, movies
                else:
                    print("Task Id Not Found")
            else:
                print("Invalid Task Id")

        if task_inputs[current_task] == movies:
            task_list[current_task](task_inputs)
        print()
        print("Returning to the Main Menu Now.")
        print()

def user_account(users, movies, current_user):
    while True:
        print("Welcome to your user account, Below is a list of things that you can do in this account. To Select an option, just enter the id of that option to continue")
        action_list = ["Find a Movie [0]", "Purchase a Movie Ticket [1]", "Write a review [2]", "View Account Details [3]", "Exit [4]"]
        print(*action_list, sep=", ")
        action = input("What would you like to do?")
        if action.isdigit():
            action = int(action)
            if action == 0:
                print("Here is a list of the current viewing Movies: ")
                print(*movies.keys(), sep=", ")
                movie_id = input("Which movie details would you like to find (select movie by its id)? ")
                movie_id, movies = search_movies(movie_id, movies)
                print("Returning to the User Menu...")
            elif action == 1:
                users, movies = buy_ticket(users, movies, current_user)
                print("Returning to the User Menu...")
            elif action == 4:
                return users, movies, current_user
        else:
            print("Invalid Id")
        break
    return users, movies, current_user

def main(users, movies, current_user, logged_in):
    users, current_user, logged_in = login(users, current_user, logged_in)
    if logged_in == True:
        if current_user == "admin":
            account = input("Would you like to access User or Admin account? ")
            if account == "Admin":
                users, movies = admin_account(users, movies)
            elif account == "User":
                users, movies, current_user = user_account(users, movies, current_user)
        else:
            user_account(users, movies, current_user)
    return

main(users, movies, current_user, logged_in)