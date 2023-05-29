from wfc import Customer
from wfc import Booking

Booking()


if __name__ == '__main__':
    print("*** Hello, Welcome to the Weekend Fitness Club ***")
    while True:
        print("\nPress 1 to book a session\nPress 2 to manage your bookings"
              "\nPress 4 for monthly report\nPress 5 to exit")

        user_input = input(">>> ")

        if user_input == '1':
            Booking.new_booking()
