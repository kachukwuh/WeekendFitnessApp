class Session:
    def __init__(self,
                 session_id: str,
                 name: str,
                 day: str,
                 time: str,
                 price: float,
                 week: int,
                 reviews: list,
                 ratings: list,
                 available_slots: int,
                 booked_customers: list,
                 attended_customers_list: list,
                 attended_customers_count: int):

        self.session_id = session_id
        self.name = name
        self.day = day
        self.time = time
        self.price = price
        self.week = week
        self.reviews = reviews
        self.ratings = ratings
        self.available_slots = available_slots
        self.booked_customers = booked_customers
        self.attended_customers_list = attended_customers_list
        self.attended_customers_count = attended_customers_count
