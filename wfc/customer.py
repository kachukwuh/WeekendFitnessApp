from random import choice


class Customer:
    def __init__(self, first_name: str, last_name: str, year_of_birth: int, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.email = email
        self.booking_ids: dict = {}
        self.reviews: dict = {}

    def greet_customer(self):
        print(f"Hi, my name is {self.first_name} and I am {2023 - self.year_of_birth} years old")

    @staticmethod
    def generate_uid():
        choices: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        uid: str = ""
        for char in range(7):
            uid += choice(choices)
        return uid
