from .session import Session
from .customer import Customer


def get_prices(fitness):
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
                                get_prices(fitness_type), week, [], [], 5, [], [], 0))


def display_prices():
    prices: str = ""
    for fitness_type, price in Booking.fitness_prices.items():
        prices += f"{fitness_type}: £{price}\n"
    return prices


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
    def new_booking():
        print("We offer Yoga, Spin, Zumba and Body-sculpt lessons every weekend, Mornings and Evenings"
              "\nPress '1' to view our friendly prices, '2' to continue booking or '3' to go back")
        while True:
            user_choice = input(">>> ")
            if user_choice == '3':
                break
            if user_choice == '1':
                print("\nSmart Choice!")
                print(display_prices())
                print("Press '2' to continue or '3' to go back")
            if user_choice == '2':
                print("\nExcellent Choice!")
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

                first_name: str = input("Enter your first name: ")
                last_name: str = input("Enter your last name: ")
                year_of_birth: int = int(input("Enter your year of birth: "))
                email_address: str = input("Enter your email address: ")

                customer = Customer(first_name, last_name, year_of_birth, email_address)
                Booking.customer_database.append(customer)
                customer_uid = customer.generate_uid()
