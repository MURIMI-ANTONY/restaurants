class Restaurant:
    all_restaurants = [] # class variable to store all instances of the class

    def __init__(self, restaurant_name):
        self._name = restaurant_name # instance variable for restaurant name
        self._reviews = [] # instance variable for restaurant reviews
        Restaurant.all_restaurants.append(self) # add instance to the class variable all_restaurants

    def name(self):
        return self._name # return the name of the restaurant

    def add_review(self, review):
        self._reviews.append(review) # add a review to the restaurant's review list

    def average_star_rating(self):
        total_rating = sum(review.rating() for review in self._reviews) # calculate the total rating of all reviews
        num_reviews = len(self._reviews) # calculate the number of reviews
        return total_rating / num_reviews if num_reviews > 0 else 0 # return the average rating or 0 if no reviews

    def reviews(self):
        return self._reviews # return the list of reviews for the restaurant

    def customers(self):
        return list({review.customer() for review in self._reviews}) # return a list of unique customers who have reviewed the restaurant

    @classmethod
    def all(cls):
        return cls.all_restaurants # return all instances of the class Restaurant