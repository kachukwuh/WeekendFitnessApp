from random import choice


class Customer:
    def __init__(self, first_name: str, last_name: str, year_of_birth: int, email_address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.email_address = email_address
        self.booking_ids: list = []
        self.reviews: dict = {}
        self.sessions_id: dict = {}
        self.attended_lessons: list = []

    @staticmethod
    def generate_uid():
        choices: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        uid: str = ""
        for char in range(7):
            uid += choice(choices)
        return uid
