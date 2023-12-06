

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
        total = sum(review.ratings() for review in self._review())
        length = len(self._review())
        mean = total / length
        if length > 0:
            return mean
        else:
            return 0
        