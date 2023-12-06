

class Review:
    reviews =[]
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
        from customer import Customer
        return self._customer
    
  
    def restaurant(self):
        from restaurant import Restaurant
        return self._restaurant

    
    @classmethod
    def all(cls):
        return cls.reviews
    
