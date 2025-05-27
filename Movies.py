import easygui

movies = {
    "Inception": {
        "Title": "Inception",
        "Genre": "Sci-Fi",
        "Duration": 148,
        "Seats": 85,
        "Rating": 6,
        "Reviews": {
            1: {"Name": "Adam", "Rating": 6, "Comment": "Amazing plot!"},
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
            1: {"Name": "Jane", "Rating": 4.6, "Comment": "Mind-expanding!"},
        },
        "Price": 13,
    },
    "Joker": {
        "Title": "Joker",
        "Genre": "Drama",
        "Duration": 122,
        "Seats": 100,
        "Rating": 8.0,
        "Reviews": {
            1: {"Name": "Jason", "Rating": 8.0, "Comment": "Dark and intense."},
        },
        "Price": 12,
    },
}
 
users = {
    "admin": {"Password": "unbirvwb", "Balance": 999999999999.99},
    "Billy": {"Password": "billy", "Balance": 1250.50},
    "Bobby": {"Password": "bobby", "Balance": 820.00},
    "Bo": {"Password": "bo", "Balance": 312.75},
}

current_user = ""
logged_in = False

def error_msg(msg):
    easygui.msgbox(msg=msg, title="Error")
    return

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
                    if password == users[user_name]["Password"]:
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
    else:
        easygui.msgbox(msg="Login Timeout. Exitting Programme...")
    return users, current_user, logged_in, attempts

def output_movies(movies, mode, movie_id=""):  
    if movie_id == "":
        msg_lines = ["|-- Showing All Movies --|\n"]
        for title, details in movies.items():
            msg_lines.append(f"\n{title}: ")
            for detail, info in details.items():
                if detail == "Reviews":
                    msg_lines.append(f"  {detail}:")
                    movie_review = []
                    for review in info.values():
                        for item, response in review.items():
                            movie_review.append(f"\t{item}: {response}")
                    msg_lines.append("\n".join(movie_review))
                else:
                    msg_lines.append(f"  {detail}: {info}")
    else:
        msg_lines = [f"|-- Showing: {movie_id} --|\n"]
        for detail, info in movies[movie_id].items():
            if detail == "Reviews":
                msg_lines.append(f"  {detail}:")
                movie_review = []
                for review in info.values():
                    for item, response in review.items():
                        movie_review.append(f"\t{item}: {response}")
                msg_lines.append("\n".join(movie_review))
            else:
                msg_lines.append(f"  {detail}: {info}")
    msg = "\n".join(msg_lines)
    if mode == "Print":
        easygui.msgbox(msg)
        return
    elif mode == "Return":
        return msg

def search_movies(movies, request=""):
    movie_options = list(movies.keys())
    msg = "What movie would you like to find?"

    movie_id = easygui.enterbox(msg, title="Find a Movie")

    if movie_id is None:
        return
    
    else:
        for movie in movie_options:
            if movie_id.lower() == movie.lower():
                if request == "Print":
                    output_movies(movies, "Print", movie)
                    return
                
                elif request == "Return":
                    return movie
        error_msg("Movie Not Found")
    return

def buy_ticket(users, movies, current_user):
    user_balance = users[current_user]["Balance"]

    msg = f"===  Here is a List of currently Viewing Movies  ===\n\n\nYour Current Balance: ${user_balance}\n\nSelect one of the Movies to Continue:\n\n"
    msg += str(output_movies(movies, "Return"))
    title = "Purchase Movie Tickets"
    choices = list(movies.keys())
    choices.append("Exit")

    while True:
        selection = easygui.buttonbox(msg, title, choices)

        if selection is None or selection == "Exit":
            return
        
        else:
            if selection in movies:
                seats_available = movies[selection]["Seats"]
                ticket_price = movies[selection]["Price"]
                user_balance = users[current_user]["Balance"]
                if seats_available > 0:

                    msg_lines = []
                    msg_lines.append(f"Seats Available: {seats_available}")
                    msg_lines.append(f"Ticket Price: {ticket_price}")
                    msg_lines.append(f"Current Balance: {user_balance}")
                    msg = "\n".join(msg_lines)
                    msg += "\n\nHow many seats would you like to purchase?"
                    seats_wanted = easygui.enterbox(msg, title="Purchase Tickets")
                    if seats_wanted is None:
                        return
                    
                    elif check_type(seats_wanted) != "int":
                        error_msg("Invalid Input, Please enter a valid number of seats to purchase")
                        continue

                    elif int(seats_wanted) < 1:
                        error_msg("You must purchase at least 1 seat")
                        continue

                    else:
                        seats_wanted = int(seats_wanted)
                        booking_price = float(seats_wanted * ticket_price)

                        if seats_wanted > seats_available:
                            error_msg(f"There are only {seats_available} seats available for {selection}. Please enter a valid number of seats to purchase.")
                            continue

                        if seats_wanted > user_balance // ticket_price:
                            error_msg(f"You cannot afford {seats_wanted} tickets for {selection}. You can only afford {user_balance // ticket_price} tickets at ${ticket_price} each.")
                            continue

                        if user_balance >= booking_price:
                            user_balance -= booking_price
                            seats_available -= seats_wanted
                            confirm_purchase = easygui.ynbox(msg=f"You have selected {seats_wanted} tickets for {selection} at a total cost of ${booking_price}. \n\nYour new balance will be ${user_balance}. \n\n\nWould you like to confirm your purchase?", title="Purchase Confirmation")

                            if (confirm_purchase is None) or (confirm_purchase == False):
                                easygui.msgbox("Purchase Cancelled")
                                return
                            
                            elif confirm_purchase == True:
                                movies[selection]["Seats"] = seats_available
                                users[current_user]["Balance"] = user_balance
                                easygui.msgbox(f"Purchase Successful, Your new balance is ${user_balance}.")
                                continue_purchase = easygui.ynbox(msg="Would you like to purchase tickets for another movie?", title="Continue Purchase")
                                if continue_purchase is None or continue_purchase == False:
                                    return users, movies
                                else:
                                    continue
                        else:
                            exit = easygui.ynbox(msg=f"You have insufficient Funds, you need ${booking_price} to book this amount of seats. Current Balance: ${user_balance}\n\nWould you like to return to the main menu?", title="Insufficient Funds")
                            if exit is None:
                                return users, movies
                            
                            elif exit == True:
                                return users, movies
                            
                            else:
                                continue
                else:
                    try_again = easygui.ynbox("Unfortunately, this movie is fully booked out. Would you like to try another movie?", title="Movie Fully Booked")
                    if (try_again is None) or (try_again == False):
                        return users, movies
                    
                    elif try_again == True:
                        continue
            else:
                retry = easygui.ynbox("Unfortunately, this movie is already booked out. Would you like to purchase tickets for another movie?", title="Movie Not Found")
                if (retry is None) or (retry == False):
                    return users, movies
                
                elif retry == True:
                    continue

def add_review(users, movies, current_user):
    while True:
        movie_id = search_movies(movies, "Return")
        if movie_id is None:
            return users, movies

        elif movie_id in movies:
            fields = ["Name", "Rating (1-10)", "Comment"]
            defaults = [current_user, "", ""]
            while True:
                values = easygui.multenterbox(
                    "Enter your review details below:",
                    title="Add Review",
                    fields=fields,
                    values=defaults
                )
                if values is None:
                    return users, movies

                if not isinstance(values, list) or len(values) != len(fields):
                    error_msg("Please fill in all fields.")
                    continue

                name, rating, comment = values

                if not name.strip():
                    error_msg("Name cannot be empty.")
                    continue

                if check_type(rating) not in ["float", "int"]:
                    error_msg("Rating must be a number between 1 and 10.")
                    continue
                
                rating_val = float(rating)
                if not (1 <= rating_val <= 10):
                    error_msg("Rating must be between 1 and 10.")
                    continue

                if not comment.strip():
                    error_msg("Comment cannot be empty.")
                    continue

                review = {
                    "Name": name,
                    "Rating": rating_val,
                    "Comment": comment
                }

                if "Reviews" not in movies[movie_id]:
                    movies[movie_id]["Reviews"] = {}

                review_id = len(movies[movie_id]["Reviews"]) + 1
                movies[movie_id]["Reviews"][review_id] = review

                easygui.msgbox(f"Review added successfully for {movie_id}!", title="Review Added")
                return users, movies
        else:
            error_msg("Movie Not Found")

def view_details(users, current_user):
    show_password = False
    while True:
        msg = f"--- Account Details ---\n"
        msg += f"Username: {current_user}\n"
        for key, value in users[current_user].items():
            if key == "Password":
                if show_password:
                    msg += f"{key}: {value}\n"
                else:
                    hidden_pw = "*" * len(str(value))
                    msg += f"{key}: {hidden_pw}\n"
            elif key == "Balance":
                msg += f"{key}: ${value:,.2f}\n"
            else:
                msg += f"{key}: {value}\n"

        # Use if-else for toggle label
        if show_password:
            toggle_label = "Hide Password"
        else:
            toggle_label = "Show Password"

        choice = easygui.buttonbox(
            msg,
            title="User Details",
            choices=[toggle_label, "Ok"]
        )
        if choice == "Ok" or choice is None:
            break
        elif choice == toggle_label:
            show_password = not show_password
    return

def add_movie(movies):
    while True:
        fields = ["Title", "Genre", "Duration (minutes)", "Seats", "Price"]
        values = easygui.multenterbox("Enter new movie details:", "Add Movie", fields)
        if values is None:
            return movies
        
        if not isinstance(values, list) or len(values) != len(fields):
            error_msg("Please fill in all fields.")
            continue

        movie_title, movie_genre, movie_duration, movie_seats, movie_price = values

        if not all([movie_title, movie_genre, movie_duration, movie_seats, movie_price]):
            error_msg("All fields must be filled.")
            continue

        msg = (
            f"New Movie Details:\n\n"
            f"Title: {movie_title}\n"
            f"Genre: {movie_genre}\n"
            f"Duration: {movie_duration}\n"
            f"Number of Seats: {movie_seats}\n"
            f"Ticket Price: {movie_price}\n"
        )
        confirmation = easygui.ynbox(msg + "\nConfirm?", title="Confirm Movie")
        if confirmation:
            movies[movie_title] = {
                "Title": movie_title,
                "Genre": movie_genre,
                "Duration": movie_duration,
                "Seats": int(movie_seats),
                "Rating": 0,
                "Reviews": {},
                "Price": float(movie_price)
            }
            easygui.msgbox("Movie added successfully!")
            return movies
        else:
            retry = easygui.ynbox("Would you like to try again?", title="Retry?")
            if not retry:
                return movies

def edit_movie(movies):
    while True:
        movie_titles = list(movies.keys()) + ["Cancel"]
        target = easygui.buttonbox("Select a movie to edit:", "Edit Movie", movie_titles)
        if target is None or target == "Cancel":
            return movies
        details = movies[target]

        msg = f"{target} Selected.\n\nMovie Details:\n"
        for key in ["Title", "Genre", "Duration", "Seats", "Reviews", "Price"]:
            msg += f"{key}: {details.get(key)}\n"
        options = ["Title", "Genre", "Duration", "Seats", "Reviews", "Price", "Cancel"]
        selection = easygui.buttonbox(
            msg + "\nSelect an item to edit:",
            title="Edit Movie",
            choices=options
        )
        if selection is None or selection == "Cancel":
            return movies
        if selection in options[:-1]:
            change = easygui.enterbox(f"What would you like {selection} to be?", "Edit Movie")
            if change is None:
                continue
            else:
                movies[target][selection] = change
                easygui.msgbox("Change Successful")
        else:
            easygui.msgbox("Invalid Item")

def view_users(users):
    user_display = []
    for user in users.keys():
        if user == "admin":
            continue
        else:
            user_display.append(user)
    
    if not user_display:
        easygui.msgbox("No users to display.", "View Users")
        return users

    msg_lines = ["--- Current Users ---\n"]
    for user in user_display:
        details = users[user]
        msg_lines.append(f"Username: {user}")
        for key, value in details.items():
            if key == "Balance":
                msg_lines.append(f"  {key}: ${value:,.2f}")
            else:
                msg_lines.append(f"  {key}: {value}")
        msg_lines.append("")

    msg = "\n".join(msg_lines)
    goto_edit_users = easygui.ynbox(msg + "\nWould you like to edit this list?", "View Users")
    if goto_edit_users:
        users = edit_users(users)
    return users

def edit_users(users):
    while True:
        users_list = list(users.keys())
        users_list.append("Cancel")
        user = easygui.buttonbox("Which user would you like to edit?", "Edit User", users_list)
        if user is None:
            return users
        if user in users.keys():
            user_info = users[user]
            msg = f"Editing {user}:\n"
            for item in user_info.keys():
                msg += f"{item}: {user_info[item]}\n"
            # Use buttonbox for attribute selection
            attributes = list(user_info.keys()) + ["Cancel"]
            change_id = easygui.buttonbox(
                msg + "\nSelect an attribute to edit:",
                title="Edit User",
                choices=attributes
            )
            if change_id is None or change_id == "Cancel":
                return users
            if change_id in user_info.keys():
                change = easygui.enterbox(f"What would you like to change {change_id} to?")
                if change is not None:
                    user_info[change_id] = change
                    easygui.msgbox("Changing Detail Now.")
                repeat = easygui.ynbox("Is there any other changes you would like to make?", title="Edit Again?")
                users[user] = user_info
                if not repeat:
                    break
            else:
                easygui.msgbox("Invalid item")
        else:
            easygui.msgbox("User Not Found")
    return users

def admin_account(users, movies):
    while True:
        action_list = [
            "Add Movie [0]", 
            "Edit Movie [1]", 
            "View User Details [2]", 
            "Edit User Details [3]", 
            "Return to Main Menu [4]"
        ]
        action = easygui.buttonbox(
            msg="Welcome to the admin account. Below is a list of things you can do.\n\nSelect an option to continue:",
            title="Admin Menu",
            choices=action_list
        )
        if action is None:
            break
        
        action = str(action)
        index = action_list.index(action)
        if index == len(action_list) - 1:
            break

        function_list = [
            add_movie,
            edit_movie,
            view_users,
            edit_users
        ]
        variable_list = [
            movies,
            movies,
            users,
            users
        ]

        # Call the selected function and update the relevant variable
        if index in [0, 1]:  # Movie functions
            movies = function_list[index](movies)
        elif index in [2, 3]:  # User functions
            users = function_list[index](users)

    return users, movies

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
        
        if action == None:
            break

        action = str(action)
        index = action_list.index(action)

        if index == len(action_list) - 1:
            break

        function_list = [
            lambda: search_movies(movies, "Print"), 
            lambda: buy_ticket(users, movies, current_user), 
            lambda: add_review(users, movies, current_user), 
            lambda: view_details(users, current_user)
            ]
        variable_list = [
            None,
            [users, movies],
            [users, movies],
            None
        ]

        if action in action_list:
            if variable_list[index] == None:
                function_list[index]()
            else:
                variable_list[index] = function_list[index]()

    return users, movies, current_user

def main(users, movies, current_user, logged_in):
    while True:
        attempts = 0
        users, current_user, logged_in, attempts = login(users)
        if logged_in == True and attempts < 5:
            if current_user == "admin":
                while True:
                    account = easygui.buttonbox(
                        msg="Would you like to access the User or Admin account?",
                        title="Account Selection",
                        choices=["Admin", "User", "Logout"]
                    )
                    if account == "Admin":
                        users, movies = admin_account(users, movies)
                    elif account == "User":
                        users, movies, current_user = user_account(users, movies, current_user)
                    else:
                        break
            else:
                users, movies, current_user = user_account(users, movies, current_user)
        else:
            break
    return

main(users, movies, current_user, logged_in)