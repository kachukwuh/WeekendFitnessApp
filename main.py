from wfc import Booking
Booking()

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
            if customer is None:
                print("\nSorry, we have no such records, please do register\n")
                continue
            user_choice = Booking.manage_bookings(customer)
            if user_choice == '1':
                pass
            if user_choice == '2':
                pass
            if user_choice == '3':
                continue
            else:
                print("\nSorry, Invalid Entry\n")
            continue
        if user_choice == '3':
            print("Thank You, Goodbye")
            break
        print("\nSorry, Invalid Entry\n")
