from .session import Session
from .customer import Customer


# Getting the price for each fitness type in generate_sessions()
def get_prices(fitness: str):
    for key, value in Booking.fitness_prices.items():
        if key == fitness:
            return value


# Helper function to generate session id: used in generate_sessions()
def generate_session_id(fitness_type: str, week: int, day: str, session: str):
    return f"{fitness_type}{week}{day[:2]}{session[0]}"


# Function to create a database of the different sessions offered
# Each session has a session_id, fitness_type, day, time, price and week
def generate_sessions():
    # Creating each session e.g. Saturday morning Yoga session
    for week in range(1, Booking.weeks + 1):
        for fitness_type in Booking.fitness_types:
            for day in Booking.days:
                for session in Booking.sessions:
                    Booking.sessions_database.append(
                        Session(generate_session_id(fitness_type, week, day, session), fitness_type, day, session,
                                get_prices(fitness_type), week))


# Helper function to display the prices of each fitness type: Used in book_customer()
def display_prices():
    prices: str = ""
    for fitness_type, price in Booking.fitness_prices.items():
        prices += f"Our {fitness_type} lessons are only £{price}\n"
    return prices


# Helper function that uses a booking_id to return a session: Used in manage_bookings()
def get_current_session(booking_id: str):
    for session in Booking.sessions_database:
        if booking_id in session.booked_customers:
            return session
    return None


class Booking:
    fitness_types: list = ["Yoga", "Spin", "Zumba", "Body-sculpt"]
    fitness_prices: dict = {"Yoga": 12.00, "Spin": 11.75, "Zumba": 10.50, "Body-sculpt": 11.25}
    days: list = ["Saturday", "Sunday"]
    sessions: list = ["Morning", "Evening"]
    weeks: int = 8
    sessions_database: list = []
    customer_database: list = []

    def __init__(self):
        # Generates sessions database on start up
        generate_sessions()

    # Checks if customer is in the database using their email, if not, creates a new customer and returns the customer
    @staticmethod
    def register_customer():
        email_address: str = input("Enter your email address: ")

        for customer in Booking.customer_database:
            if customer.email_address == email_address:
                return customer

        while True:
            first_name: str = input("Enter your first name: ").capitalize()
            if first_name:
                break
            else:
                print("Please enter a valid first name")
                continue

        while True:
            last_name: str = input("Enter your last name: ").capitalize()
            if last_name:
                break
            else:
                print("Please enter a valid last name")
                continue

        while True:
            year_of_birth: int = input("Enter your year of birth: ").isdigit()
            if year_of_birth:
                year_of_birth = int(year_of_birth)
                break
            else:
                print("Please enter a valid year of birth")

        customer = Customer(first_name, last_name, year_of_birth, email_address)
        Booking.customer_database.append(customer)
        return customer

    # Customer Sign-In: Returns a customer if in database, if not, returns None
    @staticmethod
    def customer_sign_in():
        email_address: str = input("Enter your email address: ")

        for customer in Booking.customer_database:
            if customer.email_address == email_address:
                return customer
            return None

    # Book a customer for session: Receives a customer and books them after some verifications
    @staticmethod
    def book_customer(customer: Customer):
        print(f"\nWelcome, {customer.first_name}\nWe offer Yoga, Spin, Zumba and Body-sculpt lessons every "
              f"weekend, Mornings and Evenings")
        while True:
            user_choice = input("Press '1' to view our friendly prices, '2' to continue or '3' to go back\n>>> ")
            if user_choice == '3':
                break
            if user_choice == '1':
                print("\nSmart Choice!\n")
                print(display_prices())
                user_choice = input("Press '2' to continue or '3' to go back\n>>> ")
            if user_choice == '2':
                print("\nExcellent Choice!\n")
                while True:
                    fitness_choice = input("Enter 'Yoga', 'Spin', 'Zumba' or 'Body-sculpt' to book\n>>> ").capitalize()
                    if fitness_choice in Booking.fitness_types:
                        break
                    print("Sorry, Invalid Entry")
                while True:
                    try:
                        week_choice = int(input("Enter week '1', '2', '3', '4', '5', '6', '7' or '8'\n>>> "))
                        if week_choice in range(1, Booking.weeks + 1):
                            break
                    except ValueError:
                        print("Sorry, Invalid Entry, enter a digit from 1 - 8")
                while True:
                    day_choice = input("Enter 'Saturday' or 'Sunday'\n>>> ").capitalize()
                    if day_choice in Booking.days:
                        break
                    print("Sorry, Invalid Entry")
                while True:
                    session_choice = input("Enter 'Morning' or 'Evening'\n>>> ").capitalize()
                    if session_choice in Booking.sessions:
                        break
                    print("Sorry, Invalid Entry")

                session_id = generate_session_id(fitness_choice, week_choice, day_choice, session_choice)

                for session in Booking.sessions_database:
                    if session.session_id == session_id and session.available_slots < 1:
                        print("Sorry, booking unsuccessful: Session fully booked.")
                        break

                if session_id in customer.sessions_id.keys():
                    print("Sorry, booking unsuccessful: Session already booked or cancelled.")
                    break

                customer_uid = customer.generate_uid()
                for session in Booking.sessions_database:
                    if session.session_id == session_id:
                        session.available_slots -= 1
                        session.booked_customers.append(customer_uid)
                customer.booking_ids.append(customer_uid)
                customer.sessions_id.update({session_id: "booked"})
                print(f"Thank you, booking successful. Booking ID: {customer_uid}\n")
                break

    # Manage bookings: Receives a customer, asks for a booking_id and returns a particular booked session and booing_id
    @staticmethod
    def manage_bookings(customer: Customer):
        print(f"\nWelcome {customer.first_name}")
        while True:
            booking_id: str = input("Please enter the booking ID to manage a booking or 'back' to go back\n>>> ")
            if booking_id == "back":
                return "back"

            current_session: Session = get_current_session(booking_id)

            if current_session:
                print(f"\nBooking found! You have a booking for {current_session.day} {current_session.time}, "
                      f"week {current_session.week}: {current_session.name} lesson")
                return current_session, booking_id
            else:
                print("Sorry, booking not found, check the ID and try again")

    # Attend a session: Receives a customer and a session + booking_id, also allows room reviews and ratings
    @staticmethod
    def attend_session(customer: Customer, current_session):
        session: Session = current_session[0]
        booking_id: str = current_session[1]

        session.available_slots += 1
        session.attended_customers_count += 1
        session.attended_customers_list.append(customer)

        customer.booking_ids.remove(booking_id)
        customer.sessions_id.update({session.session_id: "attended"})
        customer.attended_lessons.append(session.session_id)

        user_choice = input("Thank you for attending this session\nPress '1' to leave a review or '2' to leave\n>>> ")
        if user_choice == '2':
            print("Thank you for coming, Goodbye")
        else:
            review: str = input("Please leave a review\n>>> ")
            session.reviews.append(review)
            customer.reviews.update({session.session_id: review})
            while True:
                rating: str = input("Please leave a rating: 1: Very dissatisfied, 2: Dissatisfied, 3: Ok, "
                                    "4: Satisfied, 5: Very Satisfied\n>>> ")
                if rating.isdigit() and int(rating) in range(1, 6):
                    session.ratings.append(rating)
                    customer.ratings.update({session.session_id: rating})
                    print("Thank you for your time, Goodbye")
                    break
                else:
                    print("Sorry, Invalid Entry")

    # Cancel session: Receives a customer and a session + booking_id
    @staticmethod
    def cancel_session(customer: Customer, current_session):
        session: Session = current_session[0]
        booking_id: str = current_session[1]

        session.available_slots += 1
        session.booked_customers.remove(booking_id)

        customer.booking_ids.remove(booking_id)
        customer.sessions_id.update({session.session_id: "cancelled"})

        print("Booking cancelled successfully, Goodbye")
