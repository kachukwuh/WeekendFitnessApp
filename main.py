from wfc import Booking
from wfc import Customer
from wfc import Session
Booking()

if __name__ == '__main__':
    print("*** Welcome to the Weekend Fitness Club ***")

    while True:
        user_choice: str = input("Press '1' to book a session\nPress '2' to manage bookings\nPress '3' to quit\n>>> ")
        if user_choice == '1':
            customer: Customer = Booking.register_customer()
            Booking.book_customer(customer)
            continue
        if user_choice == '2':
            customer: Customer = Booking.customer_sign_in()
            if customer is None:
                print("\nSorry, we have no such records, please do register\n")
                continue
            current_session: Session = Booking.manage_bookings(customer)
            if current_session == "back":
                continue

            user_choice = input("Press '1', to attend session, '2' to cancel or '3' to go back\n>>> ")

            if user_choice == '1':
                Booking.attend_lesson(customer, current_session)
                continue
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
