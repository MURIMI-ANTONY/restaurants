
from customer import Review
class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._view_rating = rating
        Review.reviews.append(self)
        customer.add_review(restaurant, rating)
        restaurant.add_review(self)

    def ratings(self):
        return self._view_rating

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.reviews

    
