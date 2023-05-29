class Session:
    def __init__(self, session_id: str, name: str, day: str, time: str, price: float, week: int):

        self.session_id = session_id
        self.name = name
        self.day = day
        self.time = time
        self.price = price
        self.week = week
        self.reviews: list = []
        self.ratings: list = []
        self.available_slots: int = 5
        self.booked_customers: list = []
        self.attended_customers_list: list = []
        self.attended_customers_count: int = 0
