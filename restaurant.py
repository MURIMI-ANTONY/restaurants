from review import Review

class Restaurant():
    all_restaurants =[]
    def __init__(self,restaurant_name) -> None:
        self._name = restaurant_name
        self._reviews=[]
        Restaurant.all_restaurants.append(self)

    def rest_name(self):
        return self._name
    
    def reviews(self):
        return self._reviews
    
    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)
    
    @classmethod
    def all(cls):
        return cls.all_restaurants
    
    def average_star_rating(self):
        total_rating = sum(review.ratings() for review in self._reviews)
        num_reviews = len(self._reviews)
        if num_reviews > 0:
            return total_rating / num_reviews
        else:
            return 0
        