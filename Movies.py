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
        "Genre": "Sci-Fi",
        "Duration": 169,
        "Seats": 110,
        "Rating": 4.6,
        "Reviews": {
            1: {"name": "Jane", "rating": 4.6, "comment": "Mind-expanding!"},
        },
        "price": 13,
    },
    "Joker": {
        "Title": "Joker",
        "Genre": "Drama",
        "Duration": 122,
        "Seats": 100,
        "Rating": 8.0,
        "Reviews": {
            1: {"name": "Jason", "rating": 8.0, "comment": "Dark and intense."},
        },
        "Price": 12,
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

def error_msg(msg):
    easygui.msgbox(msg=msg, title="Error")
    return

def login(users, current_user="", logged_in=False, attempts=0):
    if logged_in == True:
        return users, current_user, logged_in, attempts
    while attempts < 5:
        error = ""
        user_name = easygui.enterbox(msg="Welcome! Please Enter Username to continue", title="Login")
        if user_name is None:
            break
        elif user_name:
            if user_name in users.keys():
                password = easygui.passwordbox(msg="Enter Password", title="Login")
                if password is None:
                    continue
                elif password:
                    if password == users[user_name]["password"]:
                        easygui.msgbox("Login Successful")
                        return users, user_name, True, attempts
                    else:
                        error = "Incorrect Password"
                else:
                    error = "Missing: Password"
            else:
                error = "Username Not Found"
        else:
            error = "Missing: Username"
        error_msg(error)
        attempts += 1
        users, current_user, logged_in, attempts = login(users, current_user, logged_in, attempts)
    else:
        easygui.msgbox(msg="Login Timeout. Exitting Programme...")
    return users, current_user, logged_in, attempts

def output_movies(movies, mode, movie_id=""):  
    if movie_id == "":
        msg_lines = ["|-- Showing All Movies --|"]
        for title, details in movies:
            msg_lines.append(f"\n{title}: ")
            for detail, info in details:
                if detail == "Reviews":
                    msg_lines.append(f"\t{detail}")
                    for item, response in detail:
                        msg_lines.append(f"\t\t{item}: {response}")
                else:
                    msg_lines.append(f"\t{detail}: {info}")
    else:
        msg_lines = [f"|-- Showing: {movie_id} --|"]
        for detail, info in movies[movie_id]:
            if detail == "Reviews":
                msg_lines.append(f"\t{detail}")
                for item, response in detail:
                    msg_lines.append(f"\t\t{item}: {response}")
            else:
                msg_lines.append(f"\t{detail}: {info}")
    msg = "\n".join(msg_lines)
    if mode == "Print":
        easygui.msgbox(msg)
        return
    elif mode == "Return":
        return msg

def search_movies(movies):
    sep = ", "
    movie_options = sep.join(list(movies.keys()))
    msg = f"Movie Options are: {movie_options}\nWhat movie would you like to find?"
    movie_id = easygui.enterbox(msg, title="Find a Movie")
    if movie_id is None:
        return
    else:
        found = False
        for movie in movies.keys():
            if movie_id.lower() == str(movie).lower():
                found = True
                output_movies(movies, "Print", movie)
        if found == False:
            error_msg("Movie Not Found")
    return

def buy_ticket(users, movies, current_user):
    msg = output_movies(movies, "Return")
    while True:
        selection = ("Which movie would you like to purchase tickets for? ")
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

def check_type(input_value):
    try:
        int(input_value)
        return "int"
    except ValueError:
        pass

    try:
        float(input_value)
        return "float"
    except ValueError:
        pass

    return "str"
            

def add_review(users, movies, current_user):
    while True:
        print(movies.keys())
        movie_input = input("Which Movie Would you like to write a review for?")
        if movie_input in movies:
            user_rating = input("What would you like to rate this movie out of 10.0?")
            while True:
                if check_type(user_rating) == "float":
                    user_rating = float(user_rating)
                    if 0.0 <= user_rating <= 10.0:
                        user_review = input("What would you like to say about this movie? ")
                        user_review_list = {"name": current_user, "rating": user_rating, "comment": user_review}
                        movies[movie_input]["Reviews"].append(user_review_list)
                        total_rating = 0.0
                        for item in movies[movie_input]["Reviews"]:
                            total_rating += item["rating"]
                        new_rating = total_rating / len(movies[movie_input]["Reviews"])
                        movies[movie_input]["Rating"] = new_rating
                else:
                    print()

def view_details(users, current_user):
    msg = f"Username: {current_user}"
    for key, value in users[current_user]:
        msg += f"{key}: {value}"
    easygui.msgbox(msg, title="User Details")
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
        action_list = [
            "Find a Movie [1]", 
            "Purchase a Movie Ticket [2]", 
            "Write a review [3]", 
            "View Account Details [4]", 
            "Logout [5]"
            ]
        action = easygui.buttonbox(
            msg="Welcome to your user account, Below is a list of things that you can do in this account. \n\nSelect an option to continue",
            title="User Menu",
            choices=action_list
            )
        function_list = [
            lambda: search_movies(movies), 
            lambda: buy_ticket(users, movies, current_user), 
            lambda: add_review(users, movies, current_user), 
            lambda: view_details(users, current_user)
            ]
        if (action is None) or (action is action_list[-1]):
            break
        if action in action_list:
            action = str(action)
            index = action_list.index(action)
            function_list[index]()

    return users, movies, current_user

def main(users, movies, current_user, logged_in):
    while True:
        attempts = 0
        users, current_user, logged_in, attempts = login(users)
        if logged_in == True and attempts < 5:
            if current_user == "admin":
                account = input("Would you like to access User or Admin account? ")
                if account == "Admin":
                    users, movies = admin_account(users, movies)
                elif account == "User":
                    users, movies, current_user = user_account(users, movies, current_user)
            else:
                user_account(users, movies, current_user)
        else:
            break
    return

main(users, movies, current_user, logged_in)