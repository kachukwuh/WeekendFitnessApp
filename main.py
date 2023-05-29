from wfc import Booking

if __name__ == '__main__':
    print("*** Welcome to the Weekend Fitness Club ***")

    while True:
        user_choice: str = input("Press '1' to book a session\nPress '2' to manage bookings\nPress '3' to quit\n>>> ")
        if user_choice == '1':
            customer = Booking.register_customer()
            Booking.book_customer(customer)
            continue
        if user_choice == '2':
            customer = Booking.customer_sign_in()
            Booking.manage_bookings(customer)
            continue
        if user_choice == '3':
            print("Thank You, Goodbye")
            break
        print("\nSorry, Invalid Entry\n")
