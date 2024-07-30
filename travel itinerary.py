# Dictionary to store user details
user_details = {
    'user1': 'password1',
    'user2': 'password2',
    # Add more users if needed
}

# Dictionary to store admin details
admin_details = {
    'username': 'admin',
    'password': 'admin123'
}

# Rest of the dictionaries
places_to_visit = {
    'Paris': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
    'London': ['Big Ben', 'British Museum', 'Tower of London'],
    'Rome': ['Colosseum', 'Vatican City', 'Trevi Fountain']
}

places_to_eat = {
    'Paris': ['Le Procope', 'L\'As du Fallafel', 'Pierre Gagnaire'],
    'London': ['Dishoom', 'The Ledbury', 'Sketch'],
    'Rome': ['Roscioli', 'Da Enzo al 29', 'Trattoria Monti']
}

places_to_stay = {
    'Paris': ['Hotel de Crillon', 'Le Bristol Paris', 'Hotel Plaza Athenee'],
    'London': ['The Ritz London', 'The Dorchester', 'Shangri-La Hotel at The Shard'],
    'Rome': ['Hotel Eden', 'Hotel Hassler', 'JK Place Roma']
}

# Dictionary to store user bookings
user_bookings = {}

# Initialize user_bookings with empty dictionaries for each user
for username in user_details:
    user_bookings[username] = {}

# Function for user login
def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_details and user_details[username] == password:
        print("Login successful.")
        # Add user functionalities here
        book_trip(username)
    else:
        print("Invalid username or password.")
        user_registration()

# Function for user registration
def user_registration():
    username = input("Enter a new username: ")
    if username in user_details:
        print("Username already exists. Please choose another one.")
    else:
        password = input("Enter a password: ")
        user_details[username] = password
        user_bookings[username] = {}  # Initialize an empty dictionary for the user's bookings
        print("Registration successful. You can now login.")

# Function for user to book a trip
def book_trip(username):
    destination = input("Enter your destination (Paris/London/Rome): ").capitalize()
    if destination in places_to_visit:
        print("\nHere are some places to visit in {}:".format(destination))
        for place in places_to_visit[destination]:
            print("- " + place)
        
        print("\nHere are some places to eat in {}:".format(destination))
        for place in places_to_eat[destination]:
            print("- " + place)

        print("\nHere are some places to stay in {}:".format(destination))
        for place in places_to_stay[destination]:
            print("- " + place)

        # Booking information
        date = input("Enter the date of your trip: ")
        num_people = input("Enter the number of people: ")

        # Store booking information in the user's bookings dictionary
        user_bookings[username][destination] = {'date': date, 'num_people': num_people}
        print("Trip booked successfully!")
    else:
        print("Sorry, we don't have information for that destination.")

# Function for admin to view user bookings
def admin_view_bookings():
    for username, bookings in user_bookings.items():
        print(f"Bookings for {username}:")
        if bookings:
            for destination, details in bookings.items():
                print(f"Destination: {destination}")
                print(f"Date: {details['date']}")
                print(f"Number of people: {details['num_people']}")
                print("-----------------------------")
        else:
            print("No bookings found for this user.")
        print()

# Function for admin login
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if username == admin_details['username'] and password == admin_details['password']:
        print("Admin login successful.")
        admin_view_bookings()  # Show bookings
    else:
        print("Invalid username or password.")

# Main program
while True:
    print("\nWelcome to the Travel Itinerary Planner")
    print("1. Plan a trip")
    print("2. Login as user/customer")
    print("3. Admin login")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        destination = input("Enter your destination (Paris/London/Rome): ").capitalize()
        if destination in places_to_visit:
            print("\nHere are some places to visit in {}:".format(destination))
            for place in places_to_visit[destination]:
                print("- " + place)
            
            print("\nHere are some places to eat in {}:".format(destination))
            for place in places_to_eat[destination]:
                print("- " + place)

            print("\nHere are some places to stay in {}:".format(destination))
            for place in places_to_stay[destination]:
                print("- " + place)
        else:
            print("Sorry, we don't have information for that destination.")

    elif choice == '2':
        login_choice = input("Do you want to login or register? (login/register): ").lower()
        if login_choice == 'login':
            user_login()
        elif login_choice == 'register':
            user_registration()
        else:
            print("Invalid choice.")

    elif choice == '3':
        admin_login()

    elif choice == '4':
        print("Thank you for using the Travel Itinerary Planner. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")