from .session import Session
from .customer import Customer


def get_prices(fitness: str):
    # Getting the price for each fitness type to use in generating sessions
    for key, value in Booking.fitness_prices.items():
        if key == fitness:
            return value


def generate_session_id(fitness_type: str, week: int, day: str, session: str):
    return f"{fitness_type}{week}{day[:2]}{session[0]}"


def generate_sessions():
    # Creating each session e.g. Saturday morning Yoga session
    for week in range(1, Booking.weeks + 1):
        for fitness_type in Booking.fitness_types:
            for day in Booking.days:
                for session in Booking.sessions:
                    Booking.sessions_database.append(
                        Session(generate_session_id(fitness_type, week, day, session), fitness_type, day, session,
                                get_prices(fitness_type), week))


def display_prices():
    prices: str = ""
    for fitness_type, price in Booking.fitness_prices.items():
        prices += f"Our {fitness_type} lessons are only £{price}\n"
    return prices


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
        generate_sessions()

    @staticmethod
    def register_customer():
        email_address: str = input("Enter your email address: ")

        for customer in Booking.customer_database:
            if customer.email_address == email_address:
                return customer

        first_name: str = input("Enter your first name: ").capitalize()
        last_name: str = input("Enter your last name: ").capitalize()
        year_of_birth: int = int(input("Enter your year of birth: "))

        customer = Customer(first_name, last_name, year_of_birth, email_address)
        Booking.customer_database.append(customer)
        return customer

    @staticmethod
    def customer_sign_in():
        email_address: str = input("Enter your email address: ")

        for customer in Booking.customer_database:
            if customer.email_address == email_address:
                return customer
            return None

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

                if session_id in customer.sessions_id:
                    print("Sorry, booking unsuccessful: Session already booked.")

                customer_uid = customer.generate_uid()
                for session in Booking.sessions_database:
                    if session.session_id == session_id:
                        session.available_slots -= 1
                        session.booked_customers.append(customer_uid)
                customer.booking_ids.append(customer_uid)
                customer.sessions_id.append(session_id)
                print(f"Thank you, booking successful. Booking ID: {customer_uid}\n")
                break

    @staticmethod
    def manage_bookings(customer: Customer):
        booking_id: str = input(
            f"\nWelcome {customer.first_name}\nPlease enter the booking ID to manage a booking\n>>> ")

        current_session: Session = get_current_session(booking_id)

        if current_session:
            print(f"Booking found!\nYou have a booking for {current_session.day} {current_session.time}, "
                  f"week {current_session.week}: {current_session.name} lesson")
            user_choice = input("Press '1', to attend session, '2' to cancel or '3' to go back\n>>> ")
            return user_choice
        else:
            print("Sorry, booking not found, check the ID and try again")
